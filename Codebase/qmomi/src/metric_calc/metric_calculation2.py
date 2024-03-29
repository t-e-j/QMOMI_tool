from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import requests
import re
from urllib.parse import urlparse
from Codebase.qmomi import get_min_click_count


class University:

	def __init__(self, uni_name, shc_url, content, links, no_of_links):
		self.uni_name = uni_name
		self.shc_url = shc_url
		self.content = content
		self.links = links
		self.no_of_links = no_of_links

	def calculate_sentiment_polarity(self):

		university_content = self.content
		polarity = TextBlob(university_content).polarity
		return round(polarity, 3)

	def calculate_sentiment_objectivity(self):

		university_content = self.content
		objectivity = 1 - TextBlob(university_content).subjectivity
		return round(objectivity, 3)

	def calculate_timeliness(self):

		timeliness = []

		if isinstance(self.links, str):
			self.links = re.findall(r"'(.*?)'", self.links)

		for url in self.links:
			result = urlparse(url)

			try:
				if True if [result.scheme, result.netloc, result.path] else False:
					header = requests.head(url).headers
					if 'Last-Modified' in header:
						last_modified = header['Last-Modified']
					else:
						# Last-modified information is not available
						last_modified = -1
				else:
					last_modified = -1

				timeliness.append(last_modified)

			except Exception as e:
				print("Unable to get the header of the web page. Error - ", e)
				return -1

		return timeliness

	def calculate_similarity(self, ideal_content):

		university_content = self.content

		# Because ideal content should match with the relevant content
		non_alphabets_list = ['_', '-', ':']
		for every_item in non_alphabets_list:
			replacing_item = " " + every_item + " "
			ideal_content = re.sub(every_item, replacing_item, ideal_content)

		corpus = [ideal_content, university_content]

		vectorizer = TfidfVectorizer()
		trsfm = vectorizer.fit_transform(corpus)

		similarity = cosine_similarity(trsfm[0], trsfm[1])

		# To get the similarity with the content with fake document
		return round(similarity[0][0], 3)

	def calculate_navigation(self, driver_path):

		min_clicks, trace = get_min_click_count(self.no_of_links, self.links, self.shc_url, driver_path)
		if min_clicks == (999, []):
			return -1, []
		return min_clicks, trace


def calculate_metrics(input_dataframe, output_dir, ideal_doc, driver_path):

	header = ['University name', 'Count of keywords matching webpages on SHC', 'Keywords matched webpages on SHC',
			  'Content on all pages', 'Similarity', 'Sentiment objectivity', 'Sentiment polarity', 'Timeliness',
			  'Navigation', 'Trace']
	output_dataframe = pd.DataFrame(columns=header)

	file = open(ideal_doc)
	ideal_content = file.read()
	file.close()

	for index, row in input_dataframe.iterrows():
		uni_name = row['University name']
		no_of_links = row['Count of keywords matching webpages on SHC']
		links = row['Keywords matched webpages on SHC']
		content = row['Relevant content on all pages']
		shc_url = row['University SHC URL']
		print("\n- ", uni_name)

		obj = University(uni_name, shc_url, content, links, no_of_links)

		print("   - Similarity")
		similarity = obj.calculate_similarity(ideal_content)

		print("   - Objectivity")
		sentiment_objectivity = obj.calculate_sentiment_objectivity()

		print("   - Polarity")
		sentiment_polarity = obj.calculate_sentiment_polarity()

		print("   - Timeliness")
		timeliness = obj.calculate_timeliness()

		print("   - Navigation")
		navigation, trace = obj.calculate_navigation(driver_path)

		output_dataframe = output_dataframe.append({'University name': uni_name,
													'Count of keywords matching webpages on SHC': no_of_links,
													'Keywords matched webpages on SHC': row['Keywords matched webpages on SHC'],
													'Content on all pages': content,
													'Similarity': similarity,
													'Sentiment objectivity': sentiment_objectivity,
													'Sentiment polarity': sentiment_polarity,
													'Timeliness': timeliness,
													'Navigation': navigation,
													'Trace': trace
													}, ignore_index=True)
	# Storing output
	output_dataframe.to_csv(output_dir + '/measures_result.csv')

	return output_dataframe

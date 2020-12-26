# QMOMI_tool #
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Student Health Centers (SHCs) websites of U.S. colleges and universities are considered high-quality and credible sources of health information by students. Although most SHC clinics comply with American College Health Association (ACHA) standards, the quality control of online health information on SHC websites is not implemented by any central governing body. <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To address this issue, we propose a new tool, QMOMI: Quantitative Measures of Online Medical Information, an open-source specialty tool that provides an efficient and multi-faceted health information quality assessment of SHC websites. QMOMI is designed and developed as a modular pipeline of three components: SHC website identification, Information collection, Quality assessment. QMOMI simply needs the university name(s) and topic(s) of interest, in the form of keyword(s), to quantify the quality of information about these topics that is posted on the SHC websites. In the first component, given university name(s) is/are used to identify the corresponding SHC website. SHC website homepages along with the set of input keyword(s) act as entry point to the second component where information related to the keywords is scraped from the SHC websites. Once we have relevant information, the third component quantifies its quality through metrics such as Readability, Objectivity, Polarity, Coverage, Similarity, and Prevalence. Accessibility and recency of the information is represented by Navigation and Timeliness metrics, respectively. <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; QMOMI tool is designed 1) to be highly efficient, scalable and repeatable so as to enable longitudinal large-scale studies that involve numerous SHC websites, 2) to be generalizable so as to enable information quality studies on any topic, and 3) to be immune to human biases by completely automating the quality quantification process. With these properties QMOMI can be used by public health administrators, researchers and practitioners to undertake nation-wide research studies, and potentially be adopted by American College Health Association (ACHA) to extend their services to SHC websites.  This project illustrates a fruitful application of computing technology to the field of public health.

## Data ##
Data can be found in the CSV files located in the Database directory. The fields of all CSVs have the following definition:

**University_name:** Name of the university for which information quality metrics are computed of a certain topic (based on input keywords).

**University SHC URL:** Student health center homepage of the university retrieved by the QMOMI.

**Keywords matched web pages on SHC:** Web page links under SHC website, on which input keywords were present.

**Count of keywords matching web pages on SHC:** Number of keywords matched web pages on SHC website.

**Total word count on all pages:** Total number of words on all the web pages under SHC, on which given keywords were found

**Reading ease:** One of the Flesch-Kincaid readability tests to quantify the reading level of the information. Higher score for FRE metric indicates easy to read material, and lower score indicates difficult to read material.

**Grade level:** Another Flesch-Kincaid readability test which corresponds to US grade levels. Lower grade level indicates easier to read the information.

**Prevalence:** Total count of all instances of all keywords found in the collected information from SHC website.

**Coverage:** Percentage of unique input keywords found on SHC website to total input keywords.

**Similarity:** The extent of the information overlap between SHC website and the ideal health information for the specific topic. This score is bounded in [0,1]. If the similarity is 1, information is identical with the ideal information. If it is 0, the information shares nothing with the ideal information.

**Sentiment objectivity:** Objectivity of the relevant information on the SHC website. This score is bounded in [0,1], where 1 is very objective and 0 is very subjective.

**Sentiment polarity:** Polarity of the relevant information on the SHC website. This score is bounded in [-1,1], where 1 means positive statement and -1 means a negative statement.

**Timeliness:** Last updated timestamps of all the web pages under SHC, on which input keywords were found. If timeliness is -1, information is not available about last update of the web page.

**Navigation:** Minimum number of clicks starting from the SHC homepage required to reach the information (related to input keywords) on SHC website. If navigation is -1, this score is not available.

**Trace:** SHC website path through which information can be reached with minimum number of clicks.

**Data found:** Boolean value to represent if information related to input keywords was found on university SHC website.

Other than these columns, there are a few columns with input keyword as a column name. These columns provide count of all occurrences of that particular keyword on the SHC website of the university.
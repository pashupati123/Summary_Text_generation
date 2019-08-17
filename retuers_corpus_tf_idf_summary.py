import nltk
import bs4 as bs  
import re
from nltk.corpus import stopwords
import heapq  
import math
from nltk.corpus import reuters
nltk.download('reuters')
from nltk import word_tokenize


def tokenize(text):
	words = word_tokenize(text)
	words = [w.lower() for w in words]
	stopwordss = set(stopwords.words('english'))
	return [w for w in words if w not in stopwordss]

def get_summary(input_txt):
	article_text=input_txt
	#article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
	article_text = re.sub(r'\s+', ' ', article_text) 
	formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
	formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
	sentence_list = nltk.sent_tokenize(article_text)
	stopwordss = set(stopwords.words('english'))

	word_frequencies = {}
	for word in nltk.word_tokenize(formatted_article_text):
		if word not in stopwordss:
			if word not in word_frequencies.keys():
				word_frequencies[word] = 1
			else:
				word_frequencies[word] += 1

	'''
	max_value=max(word_frequencies.values())
	for k in word_frequencies:
		word_frequencies[k]=float(word_frequencies[k])/max_value

	Total_number_of_sen=len(sentence_list)
 
	#calculating IDF of each token
	tf_idf_word_frequencies = {}
	for k in word_frequencies:
		tf_idf_word_frequencies[k]=word_frequencies[k]

	for k in tf_idf_word_frequencies:
		tf_idf_word_frequencies[k]=word_frequencies[k]*math.log((Total_number_of_sen/tf_idf_word_frequencies[k]),2)
	'''
	vocabulary = set()
	for file_id in reuters.fileids():
		words = tokenize(reuters.raw(file_id))
		vocabulary.update(words)
	vocabulary = list(vocabulary)
	DOCUMENTS_COUNT = len(reuters.fileids())
	word_idf = {}
	for file_id in reuters.fileids():
		words = set(tokenize(reuters.raw(file_id)))
		for word in words:
			if word not in word_idf:
				word_idf[word] = 1
			else:
				word_idf[word] += 1

	for word in vocabulary:
		word_idf[word] = word_idf[word]*math.log(DOCUMENTS_COUNT / float(1 + word_idf[word]))
	
	sentence_scores = {}
	for sent in sentence_list:
		for word in nltk.word_tokenize(sent.lower()):
			if word in word_frequencies.keys():
				if len(sent.split(' ')) < 30:
					if word not in word_idf:
						if sent not in sentence_scores.keys():
							sentence_scores[sent] = 0
					else:
						if sent not in sentence_scores.keys():
							sentence_scores[sent] = word_idf[word]
						else:
							sentence_scores[sent] += word_idf[word]


	numberof_summary_line=(len(sentence_list)*100)/100
	summary_sentences = heapq.nlargest(numberof_summary_line, sentence_scores, key=sentence_scores.get)
	summary = ' '.join(summary_sentences)
	return summary 
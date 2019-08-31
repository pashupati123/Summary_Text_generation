import nltk
import bs4 as bs  
import re
from nltk.corpus import stopwords
import heapq  
import math
import json
from nltk import word_tokenize


DOCUMENTS_COUNT=10788

def find_freq_word_in_different_doc(word):
	count_freq=0
	for i in range(1,10789):
		path="/Users/pverma/Desktop/separate_reuters_summary/separate_dict_documents/"+str(i)+".json"
		#print(path)
		with open(path) as f:
			data = json.load(f)
		doc_dict=data
		if word in doc_dict:
			count_freq+=1
	return count_freq


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
				word_freq=find_freq_word_in_different_doc(word)
				word_frequencies[word]+=word_freq

	word_idf={}
	for word in word_frequencies:
		word_idf[word]=word_frequencies[word]

	for word in word_idf:
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


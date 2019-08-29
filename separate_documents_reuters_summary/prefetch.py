import nltk
import bs4 as bs  
import re
from nltk.corpus import stopwords
import heapq  
import math
from nltk.corpus import reuters
nltk.download('reuters')
from nltk import word_tokenize
import json
from pathlib import Path


def tokenize(text):
	words = word_tokenize(text)
	words = [w.lower() for w in words]
	stopwordss = set(stopwords.words('english'))
	return [w for w in words if w not in stopwordss]

def form_idf_dict():
	doc_no=1
	for file_id in reuters.fileids():
		document="/Users/pverma/Desktop/separate_reuters_summary/separate_dict_documents/"+str(doc_no)+".json"
		Path(document).touch()
		vocabulary = set()
		word_idf = {}
		words = tokenize(reuters.raw(file_id))
		vocabulary.update(words)
		vocabulary = list(vocabulary)
		DOCUMENTS_COUNT = len(reuters.fileids())
		words = set(tokenize(reuters.raw(file_id)))
		for word in words:
			if word not in word_idf:
				word_idf[word] = 1
			else:
				word_idf[word] += 1
		for word in vocabulary:
			word_idf[word] = word_idf[word]*math.log(DOCUMENTS_COUNT / float(1 + word_idf[word]))
		if word_idf:
			with open("/Users/pverma/Desktop/separate_reuters_summary/separate_dict_documents/"+str(doc_no)+".json", 'w') as data:
				json.dump(word_idf,data)
		doc_no=doc_no+1
	
form_idf_dict()


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


word_idf = {}
def tokenize(text):
	words = word_tokenize(text)
	words = [w.lower() for w in words]
	stopwordss = set(stopwords.words('english'))
	return [w for w in words if w not in stopwordss]

def form_idf_dict():
	vocabulary = set()
	for file_id in reuters.fileids():
		words = tokenize(reuters.raw(file_id))
		vocabulary.update(words)
	vocabulary = list(vocabulary)
	DOCUMENTS_COUNT = len(reuters.fileids())
	for file_id in reuters.fileids():
		words = set(tokenize(reuters.raw(file_id)))
		for word in words:
			if word not in word_idf:
				word_idf[word] = 1
			else:
				word_idf[word] += 1
	for word in vocabulary:
		word_idf[word] = word_idf[word]*math.log(DOCUMENTS_COUNT / float(1 + word_idf[word]))
	
form_idf_dict()
with open('retures_idf_dict.json', 'w') as data:
    json.dump(word_idf,data)


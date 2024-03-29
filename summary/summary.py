import nltk
import bs4 as bs  
import re
from nltk.corpus import stopwords
import heapq  
import math

def get_summary(input_txt):
	article_text=input_txt
	article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
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

	max_value=max(word_frequencies.values())
	for k in word_frequencies:
		word_frequencies[k]=float(word_frequencies[k])/max_value

	sentence_scores = {}
	for sent in sentence_list:
		for word in nltk.word_tokenize(sent.lower()):
			if word in word_frequencies.keys():
				if len(sent.split(' ')) < 30:
					if sent not in sentence_scores.keys():
						sentence_scores[sent] = word_frequencies[word]
					else:
						sentence_scores[sent] += word_frequencies[word]
	#Divinding sentence score by toatl number of token in the sentence					
	for sent in sentence_list:
		sen_word_count=0
		for word in nltk.word_tokenize(sent.lower()):
			sen_word_count=sen_word_count+1
		if sent in sentence_scores.keys():
			sentence_scores[sent]=sentence_scores[sent]/sen_word_count
			
	numberof_summary_line=(len(sentence_list)*10)/100
	summary_sentences = heapq.nlargest(numberof_summary_line, sentence_scores, key=sentence_scores.get)
	summary = ' '.join(summary_sentences)
	return summary 

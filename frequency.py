from stopwords import *

def create_frequency_dictionary(words, cap = False):
	d = {}
	unique_words = []
	if cap == False:
		l_words = [word.lower() for word in words]
		for word in l_words:
			if word not in unique_words:
				unique_words.append(word)
		for word in unique_words:
			d[word] = l_words.count(word)
	if cap == True:
		for word in words:
			if word.istitle():
				d[word] = words.count(word)
	return d

def remove_common(words):
	filtered_words = []
	common_words = open('1000words.txt')
	common_words = common_words.read()
	for word in words:
		if word.lower() not in common_words:
			filtered_words.append(word)
	return filtered_words

def remove_stop_words(words):
	filtered_words = []
	for word in words:
		if word.lower() not in stop_words:
			filtered_words.append(word)
	return filtered_words
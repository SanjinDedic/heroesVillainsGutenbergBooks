from tokenization import *
from frequency import *
from protagonist import *
from textblob import TextBlob

def protagonist_type(candidate,book):
	score = 0
	for paragraph in create_paragraph_list(book):
		blob = TextBlob(paragraph)
		if candidate in paragraph and blob.polarity>0.5:
			score = score + 20*blob.polarity
		elif candidate in paragraph and blob.polarity<-0.5:
			score = score + 30*blob.polarity
		elif candidate in paragraph and blob.polarity>0.1:
			score = score + 10*blob.polarity
		elif candidate in paragraph and blob.polarity<-0.1:
			score = score + 20*blob.polarity
			
	if round(score) > 10:
		print(candidate,'is the hero','score:',round(score))
	elif score < 0:
		print(candidate,'is the villain','score:',round(score))
	else:
		print(candidate,'is neutral','score:',round(score))
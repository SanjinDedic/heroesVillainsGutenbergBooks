from tokenization import *
from frequency import *
from protagonist import *
from textblob import TextBlob

alice = open('jekyll.txt')
alice = alice.read()
#alice = alice[-round(0.2*len(alice)):]

#treasure = open('treasureIsland.txt')
#treasure = treasure.read()
#treasure = treasure[-round(0.2*len(treasure)):]

#jekyll = open('jekyll.txt')
#jekyll = jekyll.read()
#jekyll = jekyll[-round(0.2*len(jekyll)):]

#wizard = open('wizardOfOz.txt')
#wizard = wizard.read()
#wizard = wizard[-round(0.2*len(wizard)):]

all_words = create_word_list(alice)
filtered_words = remove_common(all_words)
freq_d = create_frequency_dictionary(filtered_words, cap = True)

ranked_list = sorted(freq_d, key = freq_d.get, reverse = True)

candidates = ranked_list[0:10] 

for candidate in candidates:
	protagonist_type(candidate, alice)

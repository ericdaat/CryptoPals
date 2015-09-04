from xor_functions import *


import urllib2

messages_array = []
scores_array = []

for line in urllib2.urlopen("http://cryptopals.com/static/challenge-data/4.txt"):
	decoded_message = decode_xor(line)
	score = 0
	for i in range(0,len(decoded_message)):
		if decoded_message[i].isalpha() :
			score += 1
	if score > 20 :
		messages_array.append(decoded_message)
		scores_array.append(score)

for i, item in enumerate(scores_array):
	if scores_array[i] == max(scores_array):
		print messages_array[i]
from xor_functions import *
import urllib2

score = 0	

for line in urllib2.urlopen("http://cryptopals.com/static/challenge-data/4.txt"):
	
	result = singleCharLineDecode(line)

	if result[1] > score :
		score = result[1]
		final_message = result[0]

print final_message
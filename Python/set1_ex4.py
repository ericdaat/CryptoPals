from xor_functions import *
import urllib2

score = 0	

for line in urllib2.urlopen("http://cryptopals.com/static/challenge-data/4.txt"):
	
	result = xor_char_decode(hex_decode(line))

	if result[2] > score :
		score = result[2]
		final_message = result[0]

print final_message
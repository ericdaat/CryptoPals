import urllib2
from xor_functions import *

def string_to_binary(string):
	return ' '.join('{0:08b}'.format(ord(x), 'b') for x in string)

def hamming_distance(string_1,string_2):
	hamming_distance = 0

	if len(string_1)==len(string_2):
		a = string_to_binary(string_1)
		b = string_to_binary(string_2)

		for i in range(0,len(a)):
			if a[i] != b[i] :
				hamming_distance += 1

	return hamming_distance

text = urllib2.urlopen("http://cryptopals.com/static/challenge-data/6.txt")
text_string = text.read()

keysize = 0
norm_hamming_distance = 1000

for temporary_keysize in range(2,40):
	part1 = text_string[0:temporary_keysize]
	part2 = text_string[temporary_keysize:2*temporary_keysize]

	temp_norm_hamming_dist = hamming_distance(part1,part2) / float(temporary_keysize)

	if temp_norm_hamming_dist < norm_hamming_distance:
		norm_hamming_distance = temp_norm_hamming_dist
		keysize = temporary_keysize

a = map(''.join, zip(*[iter(text_string)]*keysize))
transposed_a = []

for j in range(keysize):
	transposed_a.append('')
	for i in range(len(a)):
		char = a[i][j]
		transposed_a[j]+=char




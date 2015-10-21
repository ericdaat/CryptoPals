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

keysize_array = []
normalized_hamming_distance_array = []

for keysize in range(2,40):
	part1 = text_string[0:keysize]
	part2 = text_string[keysize:2*keysize]

	normalized_hamming_distance = hamming_distance(part1,part2) / float(keysize)

	keysize_array.append(keysize)
	normalized_hamming_distance_array.append(normalized_hamming_distance)

normalized_hamming_distance_array, keysize_array = zip(*sorted(zip(normalized_hamming_distance_array, keysize_array)))


best_key = keysize_array[0]

a = map(''.join, zip(*[iter(text_string)]*best_key))
transposed_a = []

for j in range(best_key):
	transposed_a.append('')
	for i in range(len(a)):
		char = a[i][j]
		transposed_a[j]+=char
from collections import Counter

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

def decode_xor(hex_string):

	decoded_string = hex_string.strip().decode("hex")
	frequency_analysis = Counter(decoded_string).most_common()
	#keep these two arrays sorted with highest score and corresponding character first
	array_score = []
	array_key = []
	decoded_message = ""

	for i in range(0,len(frequency_analysis)):
		# printing frequency analysis
		#print "%c: %i%%" %(frequency_analysis[i][0],100*frequency_analysis[i][1]/len(decoded_string))

		#trying various keys
		temporary_key = xor_strings(frequency_analysis[i][0],"e") #xoring most frequents letters in string against most frequent letter in english : 'e'
		temporary_message = "" #storing the temporary temporary_message
		temporary_score = 0
		
		for j in range (0,len(decoded_string)): #decoding with a temporary_key and storing the result in temporary_message string
			temporary_message += xor_strings(decoded_string[j],temporary_key)
			if temporary_message[j].isalpha():
				temporary_score += 1
		array_score.append(temporary_score)
		array_key.append(temporary_key)

	array_score, array_key = zip(*sorted(zip(array_score, array_key)))

	for i in range(0,len(decoded_string)):
		decoded_message += xor_strings(decoded_string[i],array_key[-1])

	return decoded_message
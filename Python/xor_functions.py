from collections import Counter

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

def hex_decode(string):
	return string.strip().decode("hex")

def xor_char_decode(input_string):
	frequency_analysis = Counter(input_string).most_common()
	message = ""
	score = 0
	key=""

	for i in range(len(frequency_analysis)):
		# printing frequency analysis
		#print "%c: %i%%" %(frequency_analysis[i][0],100*frequency_analysis[i][1]/len(input_string))

		#trying various keys
		temporary_key = xor_strings(frequency_analysis[i][0],"e") #xoring most frequents letters in string against most frequent letter in english : 'e'
		temporary_message = "" #storing the temporary temporary_message
		temporary_score = 0
		
		
		for j in range (0,len(input_string)): #decoding with a temporary_key and storing the result in temporary_message string
			temporary_message += xor_strings(input_string[j],temporary_key)
			if (temporary_message[j].isalpha() or temporary_message[j].isspace()):
				temporary_score += 1

		if temporary_score > score :
			score = temporary_score
			message = temporary_message
			key = temporary_key

	return message,key,score
from collections import Counter

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

decoded_string = hex_string.decode("hex")
frequency_analysis = Counter(decoded_string).most_common()


for i in range(0,len(frequency_analysis)):
	# printing frequency analysis
	#print "%c: %i%%" %(frequency_analysis[i][0],100*frequency_analysis[i][1]/len(decoded_string))

	#trying various keys
	key = xor_strings(frequency_analysis[i][0],"e") #xoring most frequents letters in string against most frequent letter in english : 'e'
	message = "" #storing the temporary message
	for j in range (0,len(decoded_string)): #decoding with a key and storing the result in message string
		message += xor_strings(decoded_string[j],key)
	print "try %i :using key %s : %s" %(i,key,message) #printing key and message result


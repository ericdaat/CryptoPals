from collections import Counter

input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
c = Counter(input_string).most_common()

for i in range(0,len(c)):
	print "%c: %i%%" %(c[i][0],100*c[i][1]/len(input_string))





from xor_functions import xor_strings

key = "ICE"
input_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
encoded_string = ""

for i in range(0,len(input_string)):
	key_index = i % 3
	encoded_string += xor_strings(key[key_index],input_string[i])

print encoded_string.encode("hex")
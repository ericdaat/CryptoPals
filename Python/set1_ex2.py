def hex_to_b64 (hex_string) :
	hex_in = [] #array where we store hex_string hex characters converted in binary
	b64_out = [] #array which will contain the base64 characters

	#array used to convert to base64
	std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

	for i in range (0,len(hex_string)) :
		#converting each character from hex_string in binary
		hex_in.append(bin(int(hex_string[i],16))[2:].zfill(4))

	hex_in_joined = "".join(hex_in) #joining bits all together

	i = 0;

	while i <= len(hex_in_joined)-1 :
		#grouping bits by 6
		base64_index = int(hex_in_joined[i:i+6],2)
		#converting the 6bits int into base64
		b64_out.append(std_base64chars[base64_index])
		i+=6

	#joining bits for prettier output
	b64_out_joined = "".join(b64_out)

	return b64_out_joined

# input string
hex_string2 = "1c0111001f010100061a024b53535009181c"

b64_int = hex_to_b64(hex_string2)
print b64_int
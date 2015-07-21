hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

hex_in = []
b64_out = []

std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

for i in range (0,len(hex_string)) :
	hex_in.append(bin(int(hex_string[i],16))[2:].zfill(4))

hex_in_joined = "".join(hex_in)
i = 0;

while i <= len(hex_in_joined)-1 :
	base64_index = int(hex_in_joined[i:i+6],2)
	b64_out.append(std_base64chars[base64_index])
	i+=6

b64_out_joined = "".join(b64_out)

print b64_out_joined

	








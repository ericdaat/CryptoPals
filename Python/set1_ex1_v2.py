import base64

def hex_to_b64 (hex_input):
	hex_input = hex_input.decode("hex")
	b64_output = base64.encodestring(hex_input)

	return b64_output

hex_input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print hex_to_b64(hex_input)
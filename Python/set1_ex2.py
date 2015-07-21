def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

hex_input = '1c0111001f010100061a024b53535009181c'
xor_string = '686974207468652062756c6c277320657965'

a = hex_input.decode("hex")
b = xor_string.decode("hex")

xored = xor_strings(a, b).encode("hex")
print xored
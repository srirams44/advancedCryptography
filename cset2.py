import cset1

buffer1 = "1c0111001f010100061a024b53535009181c"
buffer2 = "686974207468652062756c6c277320657965"
buffer1, buffer2 = cset1.hexToBytes(buffer1), cset1.hexToBytes(buffer2)
def fixedXOR(b1, b2):
    return bytes(x ^ y for x, y in zip(b1, b2)).hex()
print(fixedXOR(buffer1, buffer2))
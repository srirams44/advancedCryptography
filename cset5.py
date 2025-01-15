plainTXT = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"

def repeatingKeyXOR(input, key):
    input = plainTXT
    keyLen = len(key)
    encoded = []
    for i in range(0, len(input)):
        encoded.append(input[i] ^ key[i % keyLen])
    return bytes(encoded)

print("Plain text: " + str(plainTXT))
encrypted = repeatingKeyXOR(plainTXT, key).hex()
print("Encrypted: " + str(encrypted))
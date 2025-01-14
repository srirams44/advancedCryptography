import cset1

hexString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
hexString = cset1.hexToBytes(hexString)
def singleByteXOR(hex, k): #XOR's on the correct key
    return bytes(i ^ k for i in hex)
def scoreText(text): #Scores the text based on probablity
    frequencies = {
        'e': 11.1607,  'c': 4.5388,    'y': 1.7779,
        'a': 8.4966,   'u': 3.6308,    'w': 1.2899,
        'r': 7.5809,   'd': 3.3844,    'k': 1.1016,
        'i': 7.5448,   'p': 3.1671,    'v': 1.0074,
        'o': 7.1635,   'm': 3.0129,    'x': 0.2902,
        't': 6.9509,   'h': 3.0034,    'z': 0.2722,
        'n': 6.6544,   'g': 2.4705,    'j': 0.1965,
        's': 5.7351,   'b': 2.0720,    'q': 0.1962,
        'l': 5.4893,   'f': 1.8121,    ' ': 20.0
    }
    return sum(frequencies.get(chr(byte).lower(), 0) for byte in text if 32 <= byte <= 126)

bestScore, bestKey, bestPlainTXT = 0, None, None

for key in range(256): #This will try all possible single-byte keys
    decrypted = singleByteXOR(hexString, key)
    if all(32 <= byte <= 126 for byte in decrypted): #Check if all characters are printable through ASCII
        score = scoreText(decrypted)
        if score > bestScore:
            bestScore = score
            bestKey = key
            bestPlainTXT = decrypted
    else:
        continue

bestPlainTXT = bestPlainTXT.decode('ascii')
#rint("Key: " + str(bestKey))
#print("Score: " + str(bestScore))
print("Plain Text: " + str(bestPlainTXT))


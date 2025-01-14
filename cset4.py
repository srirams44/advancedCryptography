import cset1, cset3

filePath = "/Users/sriram/Downloads/4.txt"
with open(filePath, "r") as stringinput:
    data = [line.strip() for line in stringinput]

bestScore, bestKey, bestPlainTXT, bestLine = 0, None, None, None

for line in data:
    hexBytes = cset1.hexToBytes(line)
    for key in range(256):
        decrypted = cset3.singleByteXOR(hexBytes, key)
        if all(32 <= byte <= 126 or byte in (10, 13) for byte in decrypted): #Checks for ASCII printable characters, and for new with 10, 13
            score = cset3.scoreText(decrypted)
            if score > bestScore:
                bestScore = score
                bestKey = key
                bestPlainTXT = decrypted
                bestLine = line

#print("Encrypted Line: " + bestLine)
#print("Key: " + str(bestKey))
#print("Score: " + str(bestScore))
#print("Decrypted Line: " + bestPlainTXT.decode('ascii'))

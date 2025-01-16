import cset1, cset2, cset3

def hammingDistance(s1, s2):  #Calculates hamming distance
    xorResult = cset1.hexToBytes(cset2.fixedXOR(s1, s2))  #Using fixedXOR to get the result I need to compare
    return sum(bin(i).count('1') for i in xorResult)  #Count number of differing bits

"""minKey, maxKey = 20, 40  # Start from 20 instead of 2
def normalizedDistance(text, KEYSIZE):
    distances = []
    for i in range (0, len(text) - KEYSIZE * 4, KEYSIZE):  # Ensures we have at least 4 chunks
        chunk1 = text[i:i+KEYSIZE]
        chunk2 = text[i+KEYSIZE:i+2*KEYSIZE]
        chunk3 = text[i+(KEYSIZE*2):i+(KEYSIZE*3)]
        chunk4 = text[i+(KEYSIZE*3):i+(KEYSIZE*4)]

        distance1 = hammingDistance(chunk1, chunk2)  # Calculate hamming distance for the pair
        distance2 = hammingDistance(chunk3, chunk4)
        normalizeD = (distance1 + distance2) / 2
        distances.append(normalizeD)
    return sum(distances) / len(distances) if distances else 0

bestKeySize = None
bestDistance = float('inf')

for keysize in range(minKey, maxKey + 1):  # Now starts from 20 to 40
    distance = normalizedDistance(cipherTXT, keysize)
    if distance < bestDistance:
        bestDistance = distance
        bestKeySize = keysize
"""

def findKeysize(text, minK, maxK): #Finds what will probably be the best keysize, since we are told the keysize should be more than 20 bytes long, I set the minimum to 20
    bestKey , smallestDistance = 0, float('inf') #Sets a high value

    for keysize in range(minK, maxK + 1):
        chunks = [text[i:i+keysize] for i in range(0, keysize * 4, keysize)]
        distances = [ #Calculates the distance with the hammingdistance function created earlier with the 4 chunks we get in the previous line
                    hammingDistance(chunks[i],chunks[j]) / keysize
                    for i in range(len(chunks)) for j in range(i + 1, len(chunks))
        ]
        #I learnt how to do multiline list comprehension!!!
        averageDistance = sum(distances) / len(distances)

        if averageDistance < smallestDistance:
            smallestDistance = averageDistance
            bestKey = keysize

    return bestKey


def split(text, keySize):
    #This will split the ciphertext into blocks of keysize length
    return [text[i:i+keySize] for i in range(0, len(text), keySize)]

def transposeBlocks(blocks, keySize):
    #Transposes the blocks to group bytes from the same key position together
    transposed = [[] for i in range(keySize)] #Empty list for key position
    for block in blocks:
        for j in range(len(block)): #Iterates over each byte in the block
            transposed[j].append(block[j])
    return [bytes(block) for block in transposed]  # Fixed: return transposed blocks, not original blocks

def singleByteXOR(block):
    #Finds the best single byte key to decrypt a block of ciphertext, which we pass in
    bestScore, bestKey = 0, None
    for k in range(256): #Iterate over all possible byte values
        decrypted = cset3.singleByteXOR(block, k) #Xor the block
        score = cset3.scoreText(decrypted) #Score the resulting plaintext
        if score > bestScore: #Keep track of the best score and key
            bestScore = score
            bestKey = k
    return bestKey

def main():
    filePath = "/Users/sriram/Downloads/6.txt"
    with open(filePath, "r") as f:
        base64String = f.read().strip()
    cipherTXT = cset1.base64ToBytes(base64String)

    minKey, maxKey = 2, 40 #Find best keysize
    bestKeySize = findKeysize(cipherTXT, minKey, maxKey)
    print("Best Key Size: " + str(bestKeySize))

    #Split ciphertext into blocks and transpose them
    blocks = split(cipherTXT, bestKeySize)
    transposedBlocks = transposeBlocks(blocks, bestKeySize)

    #Find the repeating key by solving each transposed block
    repeatingKey = bytearray() #Stores the key in a bytearray
    for block in transposedBlocks:
        bestKey = singleByteXOR(block)
        repeatingKey.append(bestKey)

    decryptedMessage = bytes([cipherTXT[i] ^ repeatingKey[i % len(repeatingKey)]
                              for i in range(len(cipherTXT))])

    print("Repeating Key: " + str(repeatingKey.decode())) #Decodes the bytearray so it's easier to read!
    print("Decrypted Message:")
    print(decryptedMessage.decode()) #Decodes this byte array so we can read the text easier!



main()
#print("Best Key Size: " + str(bestKeySize))
#print("Best Distance: " + str(bestDistance))
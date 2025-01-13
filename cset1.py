import base64


def hexToBytes(hexString):
    bytes_result = bytes.fromhex(hexString)
    return bytes_result
def bytesToHex(bytes):
    hex_result = bytes.hex()
    return hex_result
def bytesToBase64(bytes):
    base64_result = base64.b64encode(bytes).decode('ascii')
    return base64_result
def base64ToBytes(b64String):
    bytes_result = base64.b64decode(b64String)
    return bytes_result
"""Note: Base64 encodes 3 bytes of data into 4 characters, if your input bytes arent a multiple of 3,
Base64 will pad the result with = to ensure the encoded strings length is a multiple of 4"""

hexS = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
value = (bytesToBase64(hexToBytes(hexS)))
print(value)
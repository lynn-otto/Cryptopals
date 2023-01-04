from base64 import b64encode, b64decode

#Turn string to bytes: string.encode()
#Turn hex into bytes: bytes.fromhex(hex)
#Turn b64 into bytes: b64decode(b64)
#Turn 

def to_b64(hex):
    b64 = b64encode(bytes.fromhex(hex)).decode()
    return b64

def to_hex(b64):
    hex = b64decode(b64.encode()).hex()
    return hex

def xor(bytes_1, bytes_2):
    return bytes(b1 ^ b2 for (b1,b2) in zip(bytes_1, bytes_2))

def xor_hexstrings(hex1, hex2):
    hex1_byte = bytes.fromhex(hex1)
    print(hex1_byte)
    hex2_byte = bytes.fromhex(hex2)
    print(hex2_byte)
    return xor(hex1_byte,hex2_byte)


if __name__ == '__main__':
    input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b64 = to_b64(input)
    hex = to_hex(b64)
    #print(b64)
    #print(hex)
    input2 = '1c0111001f010100061a024b53535009181c'
    input3 = '686974207468652062756c6c277320657965'
    xoring = xor_hexstrings(input2, input3)
    print(xoring.hex())
    combine = xor(b'hello', b'supersecretkey')
    #print(combine)


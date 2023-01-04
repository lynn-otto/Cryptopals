from base64 import b64encode, b64decode

def hex_to_b64(hex):
    b64 = b64encode(bytes.fromhex(hex)).decode()
    return b64

def b64_to_hex(b64):
    hex = b64decode(b64.encode()).hex()
    return hex

if __name__ == '__main__':
    input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b64 = hex_to_b64(input)
    hex = b64_to_hex(b64)
    print(b64)
    print(hex)


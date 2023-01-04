import utilities

def single_char_xor(input, char):
    key = char*len(input)
    return utilities.xor(input, key)



if __name__ == '__main__':
    input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    input_bytes = bytes.fromhex(input)
    solutions = []
    for i in range(128):
        solutions.append(single_char_xor(input_bytes, chr(i).encode()).decode())
    print(solutions)
    #print(bytes.fromhex(input).decode())
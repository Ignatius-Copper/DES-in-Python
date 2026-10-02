import base64
E_BOX = [
    31,  0,  1,  2,  3,  4,
     3,  4,  5,  6,  7,  8,
     7,  8,  9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31,  0
]
S_1 = [
    [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
    [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
    [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
    [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]
]

S_2 = [
    [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
    [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
    [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
    [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]
]

S_3 = [
    [10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
    [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
    [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
    [ 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]
]

S_4 = [
    [ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
    [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
    [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
    [ 3, 15,  0,  6, 10,  1, 13,  8,  7,  4,  5, 11, 12,  7,  2, 14]
]

S_5 = [
    [ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
    [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
    [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
    [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]
]

S_6 = [
    [12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
    [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
    [ 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
    [ 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]
]

S_7 = [
    [ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
    [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
    [ 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
    [ 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]
]

S_8 = [
    [13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
    [ 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
    [ 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
    [ 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]
]
P_BOX = [
    15,  6, 19, 20,
    28, 11, 27, 16,
     0, 14, 22, 25,
     4, 17, 30,  9,
     1,  7, 23, 13,
    31, 26,  2,  8,
    18, 12, 29,  5,
    21, 10,  3, 24
]

def f(right,round_key):
    S_BOXES = [S_1, S_2, S_3, S_4, S_5, S_6, S_7, S_8]
    new_right= "".join(f"{b:08b}" for b in right)
    result="".join(new_right[index] for index in E_BOX)
    new_round_key="".join(f"{b:08b}" for b in round_key)
    key_bit=new_round_key[:48]
    hex_result="".join(str(int(d) ^ int(k)) for d, k in zip(result, key_bit))
    slice_f=[hex_result[i:i + 6] for i in range(0, 48, 6)]
    s_box_result=""
    for index,chunk in enumerate(slice_f):
        current_s_block=S_BOXES[index]
        row=chunk[0]+chunk[5]
        collum=chunk[1:5]
        numbers_collum=int(collum,2)
        numbers_row=int(row,2)
        current_numbers=current_s_block[numbers_row][numbers_collum]
        four_bit=f"{current_numbers:04b}"
        s_box_result+=four_bit
    p_box_result="".join(s_box_result[b] for b in P_BOX)
    return p_box_result
def Des_encode(text,keyword):
    SizeOfBlock=64
    SizeOfChar=8
    ShiftKey=2
    qualityOfRounds=16
    if (len(keyword) > 0):
        keyword_bit = keyword.encode('utf-8')
        keyword_bit8=keyword_bit.ljust(8, b'\x00')
        text_bit = text.encode('utf-8')
        text_blocks = (len(text_bit)+SizeOfChar-1)//SizeOfChar
        blocks = text_blocks * SizeOfChar
        text_bit8 = text_bit.ljust(blocks, b'\x00')
        blocks_text= [text_bit8[i:i + SizeOfChar] for i in range(0, len(text_bit8), SizeOfChar)]

        for index,j in enumerate(blocks_text):
            current_key = keyword_bit8
            current_block=j
            for i in range(qualityOfRounds):
                left = current_block[:len(j) // 2]
                right = current_block[len(j) // 2:]
                new_left = right

                f_bits = f(right, current_key)
                bits = [int(f_bits[k:k + 8], 2) for k in range(0, len(f_bits), 8)]
                new_right = bytes(a ^ b for a, b in zip(left, bits))
                current_block = new_left + new_right
                head_key = current_key[:ShiftKey]
                tail_key = current_key[ShiftKey:]
                current_key = tail_key + head_key

            blocks_text[index] = current_block
        a=b''.join(blocks_text)
        base=base64.b64encode(a)
        print(base.decode('utf-8'))
        return b''.join(blocks_text)
def Des_decode(bites,keyword):
    keyword_bit = keyword.encode('utf-8')
    keyword_bit8 = keyword_bit.ljust(8, b'\x00')[:8]
    SizeOfChar = 8
    ShiftKey = 2
    qualityOfRounds = 16
    blocks_cipher  = [bites[i:i + SizeOfChar] for i in range(0, len(bites), SizeOfChar)]

    for index, j in enumerate(blocks_cipher):
        current_block = j
        current_block = j.ljust(8, b'\x00') if len(j) < 8 else j
        current_block = current_block[4:] + current_block[:4]
        current_key = keyword_bit8
        for i in range(qualityOfRounds):
            current_key= current_key[-ShiftKey:] + current_key[:-ShiftKey]

            left = current_block[:4]
            right = current_block[4:]
            new_left = right
            key=current_key
            f_bits = f(right, key)
            bits = [int(f_bits[k:k + 8], 2) for k in range(0, len(f_bits), 8)]
            new_right = bytes(a ^ b for a, b in zip(left, bits))
            current_block = new_left + new_right

        current_block = current_block[4:] + current_block[:4]

        blocks_cipher[index] = current_block
    all_bites = b''.join(blocks_cipher)
    clean_bites = all_bites.rstrip(b'\x00')
    return clean_bites.decode('utf-8', errors='ignore')

text=input("Введите текст для шифрованием DES: ")
keyword=input("Введите ключ шифрования DES: ")
encode=Des_encode(text,keyword)
decode=Des_decode(encode,keyword)
print(encode)
print(decode)
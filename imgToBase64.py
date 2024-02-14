import base64

def ordFunction(list_word):
    newwords = [ord(x) for x in list_word]
    return newwords

def numToAscii(word):
    lista = []
    for x in word:
        temporal = []
        while x != 0:
            bin = x % 2
            temporal.insert(0,bin)
            x = x // 2
        while len(temporal) < 8:
            temporal.insert(0,0)
        lista.append(temporal)
    # print(lista)
    return lista

def valXor(word,key):
        
    xorfile = []
    for i in range(len(word)):
        for j in range(8):
            if word[i][j] == key[i][j]:
                xorfile.append(0)
            else:
                xorfile.append(1)
                
    # print(xorfile)
    newlist = []
    temporal = []
    for x in xorfile:
        if len(temporal) <8:
            temporal.append(x)
        else:
            newlist.append(temporal)
            temporal = [x]
        
    if temporal:
        newlist.append(temporal)
    # print(newlist)
    
    lista = []
    for x in newlist:
        # print(x)
        x.reverse()
        # print(x)
        value = 0
        for i in range(8):
            value += 2**i * x[i]
        lista.append(value)
    # print(lista)
    
    final = []
    for x in lista:
        final.append(chr(x))
        
    # print(final)
    return final

base64_chars = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', '0', '1', '2', '3',
    '4', '5', '6', '7', '8', '9', '+', '/'
]

image = open('imagen_xor.png','rb')
image_read = image.read()
image_64_encode = base64.b64encode(image_read).decode("utf-8")
img_64_decode = base64.b64decode(image_64_encode)
# print(img_64_decode[1])
# print(format(img_64_decode[1], '08b'))
b64bits = [format(img_64_decode[i], '08b') for i in range(len(img_64_decode))]
new_b64bits = []
for x in b64bits:
    temporal = []
    for y in x:
        temporal.append(int(y))
    new_b64bits.append(temporal)
# b64bits = "".join(b64bits)
# print(b64bits)
# list_image_64_encode = list(image_64_encode)
# new_list_image_64_encode = []
# for x in list_image_64_encode:
#     indice = base64_chars.index(str(x))
#     new_list_image_64_encode.append(indice)
# print(new_list_image_64_encode)



word = new_b64bits
key = "cifrados"

if len(key) < len(img_64_decode):
    key *= len(img_64_decode) // len(key) + 1
    key = key[:len(img_64_decode)]
    
# print(key)

# wordval = ordFunction(word)
keyvalue = ordFunction(key)
# print(word)
# print(keyvalue)
# wordascii = numToAscii(wordval)
keyascii = numToAscii(keyvalue)
# print(keyascii)

xorvalue = valXor(word,keyascii)
print(xorvalue)


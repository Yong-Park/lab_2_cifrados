import base64

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
print(img_64_decode[1])
print(format(img_64_decode[1], '08b'))
# list_image_64_encode = list(image_64_encode)
# new_list_image_64_encode = []
# for x in list_image_64_encode:
#     indice = base64_chars.index(str(x))
#     new_list_image_64_encode.append(indice)
# print(new_list_image_64_encode)



# word = image_64_encode
# key = "cifrados"

# if len(key) < len(word):
#     key *= len(word) // len(key) + 1
#     key = key[:len(word)]

# wordval = ordFunction(word)
# keyvalue = ordFunction(key)
# # print(wordval)
# # print(keyvalue)
# wordascii = numToAscii(wordval)
# keyascii = numToAscii(keyvalue)

# xorvalue = valXor(wordascii,keyascii)
# print(xorvalue)


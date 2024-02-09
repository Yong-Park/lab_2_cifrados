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
    while len(word) < len(key):
        word.append([0,0,0,0,0,0,0,0])
        
    xorfile = []
    for i in range(len(word)):
        for j in range(8):
            if word[i][j] == key[i][j]:
                xorfile.append(0)
            else:
                xorfile.append(1)
                
    
    print(xorfile)

word = input("Ingrese la palabra: ")
key = input("Ingrese la clave: ")

wordval = ordFunction(word)
keyvalue = ordFunction(key)
# print(wordval)
# print(keyvalue)
wordascii = numToAscii(wordval)
keyascii = numToAscii(keyvalue)

print(wordascii)
print(keyascii)

valXor(wordascii,keyascii)

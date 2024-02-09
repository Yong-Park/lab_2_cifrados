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

def asciiToNum(word):
    lista = []
    for x in word:
        # print(x)
        x.reverse()
        # print(x)
        value = 0
        for i in range(8):
            value += 2**i * x[i]
        lista.append(value)
    # print(lista)
    return lista

def numtoLetter(word):
    final = []
    for x in word:
        final.append(chr(x))
    return final


word = input("Ingrese la palabara: ")

list_word = list(word.lower())

ordWords = ordFunction(list_word)
binarylist = numToAscii(ordWords)
decimal = asciiToNum(binarylist)
text = numtoLetter(decimal)

print(ordWords)
print(binarylist)
print(decimal)
print(text)
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

print(len(base64_chars))

def ordFunction(list_word):
    newwords = [ord(x) for x in list_word]
    return newwords
    
def numTobase64(word):
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
    final = []
    for v in lista:
        for w in v:
            final.append(w)
    # print("final: ",final)
    final_list = []
    temporal = []
    for v in final:
        if len(temporal) < 6:
            temporal.append(v)
        else:
            final_list.append(temporal)
            temporal = []
            temporal.append(v)
    if len(temporal) != 0:
        while len(temporal) < 6:
            temporal.append(0) 
        final_list.append(temporal)
    # print("final_list: ",final_list)

    listf =[]
    for x in final_list:
        x.reverse()
        value = 0
        for i in range(6):
            value += 2**i * x[i]
        listf.append(value)
    # print("listf: ",listf)
    finalend = []
    for a in listf:
        text = base64_chars[a]
        finalend.append(text)
    # print("finalend: ",finalend)
    return finalend

def base64Tonum(word):
    lista = []
    for x in word:
        lista.append(base64_chars.index(x))
    print("lista: ",lista)
    
    listanew = []
    for x in lista:
        temporal = []
        while x != 0:
            bin = x % 2
            temporal.insert(0,bin)
            x = x // 2
        while len(temporal) < 6:
            temporal.insert(0,0)
        listanew.append(temporal)
    print("listanew: ",listanew)
    list8bit = []
    for a in listanew:
        # a.pop(0)
        # a.pop(0)
        for x in a:
            list8bit.append(x)
    print("list8bit: ",list8bit)
    newlist = []
    temporal = []
    for x in list8bit:
        if len(temporal) < 8:
            temporal.append(x)
        else:
            newlist.append(temporal)
            temporal = []
            temporal.append(x)
    if len(temporal) != 0:
        while len(temporal) < 8:
            temporal.insert(0,0) 
        newlist.append(temporal)
    print("temporal: ",temporal)
    print("newlist: ",newlist)

    finallista = []
    for x in newlist:
        # print(x)
        x.reverse()
        # print(x)
        value = 0
        for i in range(8):
            value += 2**i * x[i]
        finallista.append(value)
    print("finallista: ",finallista)
    return finallista

def numtoLetter(word):
    final = []
    for x in word:
        final.append(chr(x))
    return final


word = input("Ingrese la palabara: ")

list_word = list(word)

ordWords = ordFunction(list_word)
binarylist = numTobase64(ordWords)
decimal = base64Tonum(binarylist)
text = numtoLetter(decimal)
final_text = "".join(text)

print(ordWords)
print(binarylist)
print(decimal)
print(final_text)
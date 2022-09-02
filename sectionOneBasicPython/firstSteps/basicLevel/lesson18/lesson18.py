frase = 'O rato roeu a roupa do Rei de roma'
lenFrase = len(frase) # = 34, logo índice vai até 33
x=0
newStr = ''
while x < lenFrase:
    letra = frase[x]
    print(frase[x],x)
    if letra == 'r':
        newStr += 'R'
    else:
        newStr += letra
    # newStr += frase[x] concatenação
    x+=1

print(newStr.upper())
print(newStr)

"""
array em Python
fatiamento
append, insert, pop, del, clear, extend, min, max
range
lista == array
append - insere um novo valor ao final do array
extend - 'tipo' herança
insert - insere um valor ao array porém permite que a gente defina o índice
pop - remove último item do array
del - deleta index específicos do array
range não retorna um array e sim um objeto, porém temos como transformar em array através da função list
"""

arr = [
    'davi',
    'maria',
    'Thor',
    1, #1 == bool False | 0 == bool True
    10.5,
    True
]
arr[3] = 0 #reatribuindo o valor de um índice específico.

print(arr[1][1])
print(arr)
print(arr[::-1])
print(not arr[3])

##########
print('  ')
print('Mais exemplos')

arr1 = [1,2,3]
print(arr1, '- arr1 sem extend')
arr2 = [4,5,6]
l = arr1 + arr2
arr1.extend(arr2)
print(l,'- arr1 e arr2 concatenados')
print(arr1, '- arr1 após o extend')
print(l[::-1],'- l com o passo invertido')
print(l[3],'- pegando um valor único de l')

print('  ')
print('Mais exemplos')

arr.append('itemAppendido')
print(arr, '- append')

print('  ')
print('Mais exemplos')

arr.insert(3, 'insertNoIndex3')
print(arr, '- insert')

print('  ')
print('Mais exemplos')

print(arr, '- antes do pop')
arr.pop()
print(arr,  '- depois do pop')

print('  ')
print('Mais exemplos')

arrWhile = []
print(arrWhile, '- antes de passar pelo While')
x = 0
while x <= 10:
    arrWhile.append(x)
    x+=1
print(arrWhile, '- depois de passar pelo While')
print('Array acima criado dinamicamente com WHILE')

print('  ')
print('Mais exemplos')

del(arrWhile[7:10]) #o valor do lado direito dos : indica onde vai parar, portanto não é deletado
print(arrWhile, '- com itens deletados através do del')

print('  ')
print('Mais exemplos')

arrRange = list(range(20,31))
print(arrRange, '- Array criado com Range, e transformado com list')

#Minha versão do jogo da forca na pasta exercicios, abaixo segue a resolução do professor

secreto = 'doly'
digitadas = []
chances = 3
while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFF, a letra "{letra}" não existe na palavra secreta')
        chances -= 1
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if chances == 0:
        print('Você gastou todas as suas chances! Infelizmente você perdeu!')
        break

    if secreto_temporario == secreto:
        print(f'Que legal, você descobriu a palavra secreta do Dia! A palavra era {secreto}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    print()
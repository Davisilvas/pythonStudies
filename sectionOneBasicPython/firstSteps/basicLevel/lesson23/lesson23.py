"""
abaixo segue o desempacotamento de arrays em python.

n1, n2, n3 estão pegando os index 0, 1, 2 respectivamente

*_
"""

arr = [
    'Davi',
    'Maria',
    'Doly',
    1,2,3,4,5,6,7,8,9,10
]

arr2 = [
    'Davi',
    'Maria',
    'Doly',
    1,2,3,4,5,6,7,8,9,10
]
# se for desempacotar este array, tem que por uma variável pra cada valor desse array.
# uma forma de solucionar esse problema é colocando uma variável com um * na frente. Essa variável vai retornar uma nova lista com todos os outros valores que "não foram desempacotados".
#isso de por uma variável aós a de * vai pegar o último valor do array e descompactar

n1, n2, n3, *all, n4 = arr

*nX, nn1, nn2, nn3, nn4 = arr2
# o primeiro ta pegando todos os valores do arr2 e fazendo um array novo, menos com os 4 últmos valores pois após o * vieram 4 variáveis

print(n2, all, n3, n1,n4)
print(nX)
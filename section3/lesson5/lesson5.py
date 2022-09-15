"""
FUNÇÕES ANÔNIMAS || EXPRESSÕES LAMBDA
"""

a = lambda x, y: x * y
print(a(2,4))

print('')
print('Mais exemplos')

arr = [
    ['p1', 13],
    ['p2', 50],
    ['p3', 20],
    ['p4', 15]
]

def func(item):
    return item[1] #item 1 = preços

#arr.sort(key=func) forma de ordenar usando
#arr.sort(key=func, reverse=True)
print(sorted(arr, key=lambda i: i[1], reverse=True)) #não muda o objeto original
arr.sort(key=lambda item: item[1]) #mudou a ordem da lista original
print(arr)


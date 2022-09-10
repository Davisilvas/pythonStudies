string = '012345012345012345'
n = 6
lista = [string[i: i+n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)
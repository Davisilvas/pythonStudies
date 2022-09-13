"""
Criando, lendo, escrevendo e apagando arquivos
https://docs.python.org/3/library/functions.html#open
"""

# w+ = leitura e escrita
# r a gente só lê o que tem no arquivo
# a+ ativa o append mode, add coisas no arquivo sem apagar as coisas dele


file = open('abc.txt', 'w+')  # w+ = leitura e escrita

file.write('Linha 1 \n')
file.write('Linha 2 \n')
file.write('Linha 3 \n')

file.seek(0, 0)
print('Lendo linhas:')
print(file.read())
print('###############')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('###############')


file.seek(0, 0)
print(file.readlines()) # Isso aqui vai retornar uma lista, na qual é possível iterarmos
file.seek(0, 0)
for i in file.readlines():
    print(i, end='')
file.close()

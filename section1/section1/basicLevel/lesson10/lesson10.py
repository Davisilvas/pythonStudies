# Operadores relacionais e a estrutura if
# == > >= < <= !=
# == valor igual e tipo também
x = 2
y = 3

if x != 2:
    print('x é diferente de dois')
else:
    print('x é igual a dois')

nome = input("QUAL É O SEU NOME? ")
idade = int(input('QUAL É A SUA IDADE? '))

if idade >= 18:
    print(f'O usuário {nome} pode fazer um empréstimo pois é maior de idade')
    print(type(idade))
else:
    print(f'O usuário {nome} não pode fazer um empréstimo pois é menor de idade')
"""
Estrutura de repetição while
realiza enquanto a condição é True

#SEMRPE QUE TIVER A PALAVRA CONTINUE ELE NÃO VAI MAIS EXECUTAR OS COMANDOS POSTERIORES
DIFERENTE DO CONTINUE, SEMPRE QUE O PYTHON VER A PALAVRA BREAK ELE VAI PARAR A EXECUÇÂO DO LAÇO
#PYTHON NÃO TEM O ++ COMO INCREMENTO, TEM QUE FAZER O INCREMENTO DESSA FORMA ARCAICA ACIMA - i = i + 1 - OU - i += 1 !

"""

i = 0
y = 0
"""while i <= 10:
    if i == 5:
        i += 1
        print('NESSE PONTO O i É IGUAL A 5')
        break
        #continue

    print(i)
    i += 1"""

"""while i <= 5:
    y = 0
    while y <=3:
        print(f'Neste momento o I vale {i} e o Y vale {y}')
        print(f'{i},{y}')
        y += 1
    print('_____')
    i+=1

print('Aqui o laço acabou')
"""
while True:
    v1 = input('Insira o primeiro número: ')
    v2 = input('Insira o segundo número: ')
    op = input('informe o OPERADOR: ')

    if not v1.isnumeric() or not v2.isnumeric():
        print('Por favor insira somente números!')

    v1 = int(v1)
    v2 = int(v2)

    if op == '+':
        print(f'A soma de {v1} com {v2} é igual a {v1+v2}')
    elif op == '-':
        print(f'A subtração de {v1} com {v2} é igual a {v1 - v2}')
    elif op == '*':
        print(f'A multiplicação de {v1} com {v2} é igual a {v1 * v2}')
    elif op == '/':
        print(f'A divisão de {v1} com {v2} é igual a {v1 / v2}')
    else:
        print('Por favor insira somente os operadores + - / *')

    sair = input('Deseja sair? Se sim insira [s], se não [n]: ')
    if sair == 's':
        break

print('PARABÉNS VOCÊ SAIU DO LOOP!')
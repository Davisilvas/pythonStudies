"""
n1 = input('Informe o primeiro valor: ')
n2 = input('Informe o segundo valor: ')

if type(n1) == str and type(n2) == str:
    v1 = float(n1)
    v2 = float(n2)
    if v1.is_integer() and v2.is_integer():
        r = v1+v2
        if r % 2 == 0:
            print(f'a soma resulta no número par {r}')
        else:
            print(f'o número {r} não é par')
    else:
        print('os números informados precisam ser inteiros!')
...
"""
# SOLUÇÃO DO PROFESSOR

num = input('Digite um número inteiro: ')

if num.isdigit():
    numInt = int(num)
    r = numInt % 2
    if r == 0:
        print(f'o número {numInt} é par!')
    else:
        print(f'o número {numInt} é impar!')
else:
    print('Por favor digite apenas números inteiros e positivos. Se o Sr. Usuário inserir letras, números negativos ou números decimais o progroma não vai rodar.')



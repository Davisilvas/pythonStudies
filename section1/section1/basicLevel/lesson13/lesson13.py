# func built in

n1 = input('insira um número: ')
n2 = input('insira um número: ')

# o método .isnumeric() vai checar somente números, e se eles forem positivos. E também não checa floats

"print(n1.isnumeric())"
"print(n2.isnumeric())"

if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    print(n1+n2)
else:
    print('Não foi possível converter os números para fazer a operação')
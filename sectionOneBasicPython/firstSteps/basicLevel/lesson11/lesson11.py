# operadores lógicos
# and V e V
# or F ou V
# not negação inverte o valor
# in
# not in

nome = 'Davi'

if 'D' in nome:
    print(f'Tem a letra D em {nome} - usei o in na condição')

if 'D' not in nome:
    print(f'Tem a letra D em {nome}')
else:
    print(f'Não tem a letra D em {nome} - usei o not in na condição')

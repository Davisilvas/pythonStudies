# contar quantidade de caracteres numa string
# função len - só funciona com str
# os espaços em branco contam como caracteres

usuario = input('Digite o seu nome de usuário: ')
qtd_usuario = len(usuario)

print(f"O nome de usuário é {usuario}, e este nome tem {qtd_usuario} caracteres", type(qtd_usuario))

if qtd_usuario < 5:
    print('por favor insira um nome de usuário com no mínimo 6 caracteres e máximo de 18')
elif qtd_usuario > 19:
    print('por favor insira um nome de usuário até 18 caracteres')
else:
    print('nome de usuário registrado com sucesso')


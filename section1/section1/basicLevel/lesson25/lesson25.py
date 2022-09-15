"""
operador ternário python
if numa linha só mané
"""

logged_user = False
idade = input('Qual a sua idade? ')


if not idade.isnumeric():
    print('você tem que informar apenas números o cabeção')
else:
    idade = int(idade)
    condicao = (idade >= 18)
    acesso = 'Acesso Liberado.' if condicao else 'Acesso negado, volte quando tiver 18 anos'

# msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

# if logged_user:
#     msg = 'Usuário logado.'
# else:
#     msg = 'Usuário precisa logar.'

# print(msg)
print(acesso)

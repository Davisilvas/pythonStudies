"""def greetings(name = input('Por favor nos informe o seu nome: '), saudacao='Bom dia!'):
    return f'{saudacao} {name}'"""

def greetings(nome, saudacao):
    return f'{saudacao} {nome}!'

oi = greetings('Davi','Boa tarde')

print(oi)
nome = input('Por favor nos informe o seu nome: ')
len_nome = len(nome)

if len_nome <= 4:
    print(f'{nome}, você tem um nome curto demais!')
elif len_nome >= 5 and len_nome <= 6:
    print(f'{nome}, você tem um nome de tamanho normal')
else:
    print(f'{nome}, você tem um nome longo demais!')

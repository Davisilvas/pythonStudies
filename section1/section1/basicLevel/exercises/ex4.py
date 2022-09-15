palavra = 'Doly'
acerto = []
digitadas = []
arr = [1,2,3,4]
print(len(arr))

while True:
    letra = input('Digite UMA letra: ')

    if len(letra) > 1:
        print('isso não vale, digite somente UMA letra')
    elif letra == 'd' or letra == 'D':
        print('Você acertou! A palavra tem D!')
        acerto.insert(0,'D')
    elif letra == 'o' or letra == 'O':
        print('Você acertou! A palavra tem O!')
        acerto.insert(0,'o')
    elif letra == 'l' or letra == 'L':
        print('Você acertou! A palavra tem L!')
        acerto.insert(0,'l')
    elif letra == 'y' or letra == 'Y':
        print('Você acertou! A palavra tem Y!')
        acerto.insert(0,'y')
    else:
        digitadas.append(letra)

    if len(acerto) == 4:
        print("Você achou a palavra secreta! A palavra sevreta é Doly!")
        resposta = input('Deseja SAIR do jogo? Se SIM digite s, se NÃO digite n: ')
        if resposta == 's':
            print('Você optou por sair!')
            break
        elif resposta == 'n':
            print('Você optou por continuar!')
            del(acerto[0:5 ])
            continue
        else:
            print('DIGITE APENAS S OU N')

    print(digitadas)
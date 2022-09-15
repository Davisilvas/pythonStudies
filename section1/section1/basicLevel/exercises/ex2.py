"""
hora = int(input('olá, poderia me informar que horas são?'))

if hora >= 0 and hora <= 11:
    print('Bom dia!')
elif hora >= 12 and hora <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')
"""

# SOLUÇÃO DO PROFESSOR!

hora = input('olá, poderia me informar que horas são? ')

if hora.isdigit():
    horaInt = int(hora)
    if horaInt >= 0 and horaInt <= 11:
        print('Bom dia!')
    elif horaInt >= 12 and horaInt <= 17:
        print('Boa tarde!')
    elif horaInt >= 18 and horaInt <= 23:
        print('Boa noite!')
    else:
        print('Por favor insira somente valores entre 00 e 23')
else:
    print('Por favor insira apenas números, e também somente a hora, e não os minutos!')
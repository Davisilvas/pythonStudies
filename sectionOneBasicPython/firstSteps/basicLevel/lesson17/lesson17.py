"""
while / else
o else só vai ser executado quando a condição for FALSA, se for interrompido por um break ele vai ignorar o else
"""

x = 0
acumulador = 0
# else x == 5
while x < 7 :
    #print(f'o valor de X é {x}, e o acumulador vale {acumulador}')
    print(f'o valor de X é {x}')
    #acumulador = acumulador + x
    x+=1
else:
    print('Aqui é o ELSE do loop')

print('aqui eu to FORA do loop!')
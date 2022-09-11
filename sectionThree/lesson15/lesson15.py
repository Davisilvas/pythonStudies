"""
count - itertools

(range é um iterável mas não é um iterador)
count vai te gerar um contador, que é um iterador. 

método      | Exemplo    
método start, start = 5
incremento step, step=2
o step pode ser usado pra contar de trás pra frente. step = -1
"""
from itertools import count

contador = count(start=2, step=2)

# for x in contador:
#     print(x)

#     if x >= 10:  # <- Maneira de para esse contador que vai até o infinito.
#         print('Fim da linda')
#         break

for x in contador:
    print(f'Neste momento x vale {x}')

    if x >= 15 or x <= -15:
        print('acabou, fim da linha')
        break

########## EXEMPLO DE AUTOMAÇÂO ##########
# Vamos supor que você tem uma lista, e que quer atribuir índices numéricos a essa lista. Dessa forma podemos dar um zip entre uma lista e um contador formando tuplas, e cada item vai receber um índiice pelo contador.

lista = ['Refrigerante', 'batata', 'cookie', 'manteiga', 'açúcar', 'M&M', 'Fermento Químico']
newCounter = count()

listaIndexada = zip(newCounter, lista)
print(list(listaIndexada))

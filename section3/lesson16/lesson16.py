"""
Combinatrions, permutations, e product - iterTools
Combinação - Ordem não importa
perumtação - Ordem IMPORTA
ambos não repetem valores únicos. 
produto - ordem IMPORTA e REPETE valores Únicos
itertools é um MÓDULO
"""
from itertools import combinations, permutations, product

pessoas = ['Davi', 'Maria', 'Doly', 'Thor', 'Luke']

# A seguir como descobrir todas as combinações possíveis onde ordem não importa.

for x in combinations(pessoas, 2):
    print(x)
# Como a ordem não importa, nós temos Davi, Maria. Mas não temos Maria, Davi. Como a ordem não importa e os elementos já foram juntados, não há a necessidade de fazer um Maria, Davi.

print()
print('Outro exemplo a Seguir')
print()

# A seguir como descobrir todas as combinações possíveis onde a ordem importa.

for x in permutations(pessoas, 2):
    print(x)
# Aqui vamos ter Davi, Maria e Maria, Davi. Pois como a ordem é de importância, esses dois são considerados pares diferentes.
# Porém aqui não temos a combinação de Davi, Davi pois não repete valores únicos.

print()
print('Outro exemplo a Seguir')
print()

for x in product(pessoas, repeat=2):
    print(x)

# pegou todas as combinações possíveis inclusive repetindo o mesmo valor.

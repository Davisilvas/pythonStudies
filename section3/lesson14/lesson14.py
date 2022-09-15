"""
UNINDO ITERÁVEIS.
Zip - Unindo iteráveis 
Zip_longest - itertools 

ZIP RETORNA UM ITERADOR QUE TEM O MÉTODO NEXT
"""

# Nesse caso nós temous duas listas, uma maior e uma menor. A função zip só vai unir os iteráveis até o MENOR deles acabar. Neste exemplo quando acabou a lista de estados ele parou de unir, deixando a cidade Cuiabá de fora.
# pra corrigir isso a gente importa o zip_longest. Ele vai executar com base na maior lista, porém ele vai preencher os valores faltantes com NONE.
# Para mandar um valor padrão pros lugares que seria um none a gente manda um fillvalue

from itertools import zip_longest, count

index = count()
cidades = ['Rio de Janeiro', 'Curitiba', 'Porto Alegre', 'Cuiabá']
estados = ['RJ', 'PR', 'RS']

cidadesEEstados = zip(index,cidades, estados)
cidadesEEstados2 = zip_longest(index, cidades, estados, fillvalue='Estado')

print(cidadesEEstados, type(cidadesEEstados))
for i, c, e  in cidadesEEstados:
    print(i, c, e) # < - desempacotando.

print('-' * 60)

# print(cidadesEEstados2, type(cidadesEEstados2)) 
# for i, c, e in cidadesEEstados2:
#     print(f'{i} {c} {e} ||', type(v))
# isso aqui vai gerar valores infinitos até travar o pc, pois o count é um gerador. E como estamos usando zip longest com um gerador, ele vai fivar gerando valores infinitamente. 

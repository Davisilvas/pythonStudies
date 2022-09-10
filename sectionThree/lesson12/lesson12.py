"""
iterável é algo que você pode 

Quando a gente passa o laço for numa lista ele está transformando a lista num ITERADOR.
print(hasattr(lista, '__next__')) pra saber se é um ITERADOR 

um iterável é m objeto que você pode iterar sobre ele, mas ele não necessariamente é um iterador. Não necessariamente vai te dar um valor de cada vez.
Um iterador te dá um valor de cada vez. 
CAST pra transformar em iterador iter(item)


geradores são usados quando a gente precisa manipular valores que vão usar muita memória/muiot tempo pra ser executado.

GERADORES SÃO ITERÀVEIs

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()
print(g)
<generator object gera at 0x0000025444F0DF50>

como resultado da func gera a gente tem esse gerador que esta nos dizendo onde está o objeto gerador com os dados na memória

os geradores vão reter os valores mas não vão salvar todos eles na memória, ele só vai entregar os valores quando a gente pedir esse valor. A gente pede através da função next e através das iterações. 

"""
import sys
import time

lista = list(range(100))
# print(hasattr(lista, '__iter__')) # fun pra ver se tal obj tem x coisa

print(sys.getsizeof(lista))

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

# g = gera()
# print(g)

# for v in g:
#     print(v)

#################################################

listinha = [x for x in range(1000)] # <- lista
print(type(listinha))
listinha2 = (x for x in range(1000)) # <- gerador || essa vai ter um espaço ocupado na memória de 88 bytes
print(type(listinha2))
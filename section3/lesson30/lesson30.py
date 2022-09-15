# Problema dos parêmetros mutáveis em função
# Mutáveis -> Listas, Dict
# imutáveis -> Tuplas, strings, números, Bool, None.


# Essa lista como arg padrão é o problema.
# Caso a gente tenha um argumento mutável como padrão, nós devemos trabalhar ele como, ao ato da declaração, o definir como None - que é um imutável.
# feito isso a gente converte ele no mutável que a gente deseja e o manipula. Dessa forma cada func vai retornar um valor único e não um combinado entre todas as exec.

#from dados import clients1, clients2
import dados


def clientList(clientIter, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientIter)
    return lista

def dicts(*args, dictionary=None):
    if dictionary is None:
        dictionary = {}
    dictionary.update(*args)
    return dictionary


c1 = clientList(dados.clients1)
c2 = clientList(dados.clients2)
c3 = clientList(['fulano', 'ciclano'])
d1 = dicts(dados.dict_ex)
d2 = dicts({'Name': 'Maria', 'Age': 23})
d3 = dicts({'Name': 'Doly', 'Age': 13})


print(c1)
print()
print(c2)
print()
print(c3)
print()
print(d1)
print()
print(d2)
print()
print(d3)

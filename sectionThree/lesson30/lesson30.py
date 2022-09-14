# Problema dos parêmetros mutáveis em função
# Mutáveis -> Listas, Dict
# imutáveis -> Tuplas, strings, números, Bool, None.


# Essa lista como arg padrão é o problema. 
def clientList(clientIter, lista=[]):
    lista.extend(clientIter)
    return lista


clients1 = [
    'Davi',
    'Maria',
    'Doly',
    'Thor'
]

clients2 = [
    'Davi',
    'Maria',
    'Doly',
    'Thor'
]

c1 = clientList(clients1)
c2 = clientList(clients2)
print(c1)
print(c2)

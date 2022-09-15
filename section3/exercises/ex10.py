lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

total = [sum(i) for i in zip(lista_a, lista_b)]
print(total, 'Resolução minha')
listaResultante = [x + y for x, y in zip(lista_a, lista_b)]
# -> Desempacotou a tupla e somou os itens.
print(listaResultante, 'Resolução professor')

###### FOMRA GENÉRICA ######

listaSoma = []
for i in range(len(lista_b)):
    listaSoma.append(lista_a[i] + lista_b[i])

print(listaSoma, 'Esse resultado veio da forma genérica.')

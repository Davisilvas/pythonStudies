lista = [
    ('chave', 15),
    ('chave2', 11.5)
]

d1 = {x.upper(): y*2 for x, y in lista}
print(d1)
print()
########################################################

d2 = {x: y*3 for x, y in enumerate(range(5))}
print(d2)
print()
########################################################

d3 = {x for x in enumerate(range(5))}
print(d3, type(d3))
print()
########################################################

d4 = {f'chave_{x}': x**2 for x in range(5)}
print(d4)
print()

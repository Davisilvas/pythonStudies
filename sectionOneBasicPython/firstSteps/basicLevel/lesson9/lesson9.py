# Condicionais

a = 5
b = 6
c = 7

if 2 < 5:
    print("dois é menor que 5 - entrou no IF")

if a > b:
    print("a variável A é maior que a B")
else:
    print("a variável A é menor que a B - entrou no ELSE")


if a + b == 12:
    print("A + B é 12")
elif a + b == 11:
    print("A + B é 11 - entrou no ELIF")
    if True:
        print("ENTROU NO IF ANINHADO - que é uma estrutura if dentro de outra")
else:
    print("a gente não sabe quanto é A + B")

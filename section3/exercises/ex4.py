def func(n):
    if n % 5 == 0 and n % 3 == 0:
        return 'fizzBuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    return n


y = func(25)
z = func(9)
a = func(83)
b = func(30)

print(y)
print(z)
print(a)
print(b)

#Importando Números aleatórios

from random import randint

for i in range(100):
    aleatorio = randint(0,100)
    print(func(aleatorio))

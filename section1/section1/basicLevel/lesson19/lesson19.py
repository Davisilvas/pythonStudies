"""
For in em Python
func built-in range(start (por padrão é 0), stop (onde vai parar), step (por padrão é 1))

"""

nome = 'vasco'
nomeUpper = ''

for i in nome:
    if i == 's':
        #continue/break
        nomeUpper += i.upper()
    elif i =='c':
        nomeUpper += i.upper()
    else:
        nomeUpper += i
    print(i, nomeUpper)

for x in range(13, 21, 2):
    print(x)

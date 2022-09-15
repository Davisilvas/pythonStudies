# Lists, tuples, sequences iterável
# o iterador esvazia conforme é consumido || isso vale tanto pra geredores e iteradores.
# os geradores e iteradores são feitos pra consumir apenas uma vez.

nome = 'Davi Silva Santos'

nomeGerador = (x for x in nome)
print(type(nomeGerador))
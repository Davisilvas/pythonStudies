"""
Manipulando strings pt 2
* string indices
*fatiamento [inicio:fim:passo]
funções built-in, len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo
"""

texto = 'Python_s2'

# SELECIONANDO CARACTERES A PARTIR DO ÍNDICE DELE - POSITIVO E NEGATIVO
print(texto[7]) # vai imprimir o Y que tá no índice 7!
print(texto[1]) # vai imprimir o Y que tá no índice 1!
print(texto[6]) # vai imprimir um espaço que é o que tá no índice 6!
print(texto[3]) # vai imprimir o H que tá no índice 3!
# os exemplos acima ^^ são de índices positivos
print(texto[-1])# vai imprimir o 2 pois ele é o último!
#índices negativos contam a string de trás pra frente e a partir do -1 e não do 0 como nos positivos!

# FATIANDO STRINGS
novaStr = texto[2:6]
novaStr2 = texto[:6]
novaStr3 = texto[0:6:2] #vai do 0 até o 6 pulando de 2 em 2
print(novaStr) #vai imprimir do índice 2 até o 5 (o 6 é cortado, logo a gente deve considerar pegar um índice além pra poder o que a gente quer exatamente) - o fim não é incluido.
print(novaStr2) # pra pegar o índice 0 nós ocultamos o primeiro argumento! - o mesmo para o final.
print(novaStr3)

for i in texto:
    print(i.upper())
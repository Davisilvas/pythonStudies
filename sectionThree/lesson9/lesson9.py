"""
SETS EM PYTHON

add(adiciona), update(atualiza), clear, discard
union | (une)
intersection & (todos elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos.)

os conjuntos (sets) são muito similares às listas. é uma coleção de elementos que vc pode adicionar dentro de uma mesma estrutura de dados.
a maior diferença entre sets e tuplas/listas4 é que os sets só suportam elementos únicos.

a maior diferença entre a criação de um set e dict é que o set não recebe par de key e value.

SETS não tem índices, (index). Então não da pra acessar algum valor específico. 
Mas ele pode ser iterado. Sem acessar valor específico. 

A função UPDATE vai iterar sobre o que é passado. Logo uma string vai ficar {'b','a','c'}

OS SETS NÃO RESPEITAM ORDEM. A cada hora vai aparecer de uma forma.

li = [1,1,1,1,2,3,4,4,4,'Davi','Davi']
li = set(li)
li = list(li) RESULTADO [1,2,3,4,'Davi']
"""

# SETS SUPORTAM SOMENTE ELEMENTOS IMUTÁVEIS.
s1 = {1, 2, 3, 4}
# s1 = set() <- Como criar um set vazio.
s1.add(777)
print(s1, type(s1))
s1.update('Davi')
s1.discard(3)  # <- discartei um valor ESPECÍFICO e não  um índice
print(s1, type(s1))

# Os sets podem ser usados para ELIMINAR elementos duplicados. Mas os elementos vão voltar fora de ordem.

st1 = {1, 2, 3, 4}
st2 = {1, 2, 3, 4, 5, 6}
st3 = st1 | st2  # Como UNIR dois SETS
st4 = st1 & st2  # Retorna somente os que estão presentes NOS DOIS
print(st3, 'st3')
print(st4, 'st4')

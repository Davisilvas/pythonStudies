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
"""
# SETS SUPORTAM SOMENTE ELEMENTOS IMUTÁVEIS.
s1 = {1, 2, 3, 4}
# s1 = set() <- Como criar um set vazio.


print(s1, type(s1))

s1.discard(3)  # <- discartei um valor ESPECÍFICO e não  um índice 

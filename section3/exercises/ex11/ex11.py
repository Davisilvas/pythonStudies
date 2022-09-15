from itertools import count
from operator import index

chores = []
index = count()

def add_tarefa(chore):
    chores.append(chore)
    return chores

def removerItem(ind):
    chores.pop(ind)
    return chores
    
t1 = add_tarefa('Limpar quarto')
t1 = add_tarefa('limpar pc')
t1 = add_tarefa('Lavar roupa')
t1 = add_tarefa('tirar teias')

lista_indexada = zip(index, t1)

print('\nA seguir, suas tárefas e seus index:')
for i, c in lista_indexada:
    print(f'\t{i}: {c}')

t1 = removerItem(2)
print(t1)




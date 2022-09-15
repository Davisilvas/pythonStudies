"""
Como agrupar elementos em um dicionário.
"""
from itertools import groupby, tee

# o tee faz cópia do iterador.

alunos = [
    {
        'nome': 'Davi',
        'nota': 'C'
    },

    {
        'nome': 'Maria',
        'nota': 'A'
    },

    {
        'nome': 'Doly',
        'nota': 'B'
    },

    {
        'nome': 'Thor',
        'nota': 'C'
    },

    {
        'nome': 'Tom',
        'nota': 'B'
    },

    {
        'nome': 'Mila',
        'nota': 'A'
    }
]
def ordem(item): return item['nota']


alunos.sort(key=ordem)
alunosAgrupados = groupby(alunos, ordem)

# for agrupamento, valoresAgrupados in alunosAgrupados:
#     print(f'Agrupamento: {agrupamento}')
#     for v in valoresAgrupados:
#         print(v)
#     print()

for agrupamento, valoresAgrupados in alunosAgrupados:
    va1, va2 = tee(valoresAgrupados)
    qtd = len(list(va2))

    print(f'Agrupamento: {agrupamento}')
    print(f'\t{qtd} tiraram a nota {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')
    print()

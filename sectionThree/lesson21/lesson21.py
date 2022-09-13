"""
Try / except serve pra quando houver um erro no código ele não quebrar e parar de funcionar.

Pra tratar mais de um erro na mesma exceção basta colocar elas entre ()

o else vai ser executado sempre que o código do bloco try foir executado sem lançar nenhuma exceção. Else vai ser executado sempre que o código for executado sem erros

Também temos o finally que vai ser executada SEMPRE independente de ter erro ou não.

vamos atribuir algo errado a B e tentar usar fora do bloco. Por estar fora do bloco, vai dar erro. Uma forma boa de se usar o finally é atribuindo um valor padrão para a variável, como veremos a seguir

Nós podemos ter try/except aninhado.
"""
try:
    a = {}
    b = 1/0
except NameError as erro:
    print(erro)
except (IndexError, KeyError) as erro:
    print(f'Erro de indexação ou chave -- {erro}')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print(a)
finally:
    b = None
    print('Chegou nos finalmente')

print(b)

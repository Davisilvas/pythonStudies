"""
Funções decoradas e decoradoras.
funções decoradoras vão envolver as funções que a gente quiser, mudando ou não o comportamento delas.
"""


def fala_oi():
    print('oi')


v = fala_oi
v()

print()
print('#' * 20)
print()

# Quando a função pai retorna outra função dentro dela, a gente tem que atribuir ela à uma variável a executando.


# Aqui a gente criou uma função pai, que recebe uma func com arg. Dentro do pai tem a função filho, que vai executar a func que veio como arg.

# pra prevenirmos erros na hora de passarmos argumentos em funções decoradas, nós passamos os *args, **kwargs pra fazer com que a func submissa possa receber argumentos.

# func decorador normalmente é utilizada pra adicionar algum recurso na função. Como por exemplo testar o tempo que uma func leva pra executar.
def pai(funcao):  # Func decorador
    def filho(*args, **kwargs):
        print('Função decorada')
        funcao(*args, **kwargs)
    return filho

# fala_oi = pai(fala_oi) # -> Func decorada.


@pai  # -> esse @ tem que ser com o nome da função mestre
def fala_oi2():
    print('oi2')


fala_oi2()

print()
print('#' * 20)
print()


@pai
def another(msg):
    print(msg)


another('prevenindo erros')

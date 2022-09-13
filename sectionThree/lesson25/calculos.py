import math

PI = math.pi

def dobrar_lista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

if __name__ == '__main__':
    # isso é pra evitar destes comandos serem executados em outros arquivos que importarem este módulo.
    lista = [1, 2, 3, 4, 5]
    print(dobrar_lista(lista))
    print(multiplica(lista))

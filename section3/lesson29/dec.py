from time import sleep
from time import time


def velocidade(func):
    def submissa(*args, **kwargs):
        start_time = time()
        resultado = func(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time)  # * 1000
        print(
            f'\nA função levou: {func.__name__} levou {tempo:.2f}ms pra executar.')
        return resultado
    return submissa


@velocidade  # -> decorador
def demora():  # -> decorada
    for i in range(5001):
        print(i, end='')
        # sleep(1)


demora()

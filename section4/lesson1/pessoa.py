# quando passamos uma variável sem o self, nós estamos criando uma var que é válida apenas dentro do método que ela foi criada.
# se a gente cria outro método e tenta invocar esta var que a gente criou sem o SELF a gente não vai conseguir usar, pois ela não vai existir no escopo deste outro método.
# Porém o que é declarado com o self pode ser invocado em todos os cantos da classe. Basta dar, por exemplo, um self.nome

class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        else:
            print(f'{self.nome} acabou sua refeição')
            self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo, aguarde um instante')
            return

        if self.falando:
            print(f'{self.nome} já está dialogando')
            return

        print(f'{self.nome} está livre pro diálogo e quer debater sobre {assunto}')
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        else:
            print(
                f'{self.nome} acabou seu último debate e está disponível pro próximo ')
            self.falando = False

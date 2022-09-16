# Getter obtem um valor
# Setter seta um valor
# os Getters e Setters são como se fossem uma proteção pro artibuto.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self. preco * percentual / 100)
        #print(f'O produto {self.nome} está na promoção com {percentual}% de desconto. Agora seu preço final é {self.preco}!')

    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$',''))
        self._preco = valor

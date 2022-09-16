from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self): # -> Depende da instância | obrigado a receber o SELF
        print(self.ano_atual - self.idade)
    
    @classmethod #decorador || -> Depende da Class | Obrigado a receber o CLS
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod # -> 'Uma func normal'. Porém como está dentro de uma classe a gente precisa ou de uma classe ou de uma instância pra usar-lo. Mas dentro do corpo dele a gente não pode usar nem self nem cls
    def gerar_id():
        rand = randint(10000, 19999)
        return rand
# sem self = método da CLASSE, var da CLASSE
# com self - método da INSTância var da INSTÂNCIA
# Método de classe é um factory method também, ele retorna (fabrica) o objeto pra gente também. 
# o método é relacionado à classe em geral ou à instancia?
# à classe = @classmethod
# à instância = self


import pessoa

p1 = pessoa.Pessoa('Davi', 21)
print(p1.idade)
p1.get_ano_nascimento()

p2 = pessoa.Pessoa.por_ano_nascimento('Maria', 1999)
print(p2.idade)

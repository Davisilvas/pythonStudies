# Encapsulamento serve para 'esconder' certas partes do seu código pra proteger a sua aplicação, a sua classe, método ou atributo.

# nas outras linguagens nós vamos ter modificadores de acesso. Com isso teremos métodos e atributos públicos, protected, private.

# Se o atributo estiver com apenas 1 _ na frente do nome, recomneda-se que você não acesse esse atributo

# apenas 1 _ é equivalente ao protected

# se atributo estiver com dois underlines (__) é que recomenda-se fortemente que você não mexa nesse atributo. 

#  

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    # Para acessar algo que está estritamente privado a gente pode definir um getter que vai nos retornar esses valores que queremos

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(f'Id: {id} || Nome: {nome}')

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]

# entrada de dados

#input vai receber o texto que vai ser apresentado em tela para o usuário
# tudo que for inputado sem nenhum tratamento vai ser uma str
# pra converter de str pra outro tipo de dado tem que atribuir a função a uma variável nova, assim como foi feito

nome = input("Nos informe o seu nome: ")
print(nome)
peso = float(input("Nos informe o seu peso: "))
#pesoF = float(peso)
altura = input("Nos informe a sua altura: ")
alturaF = float(altura)

imc = peso / (alturaF ** 2)

print(f"O imc de {nome} é {imc:.2f}")

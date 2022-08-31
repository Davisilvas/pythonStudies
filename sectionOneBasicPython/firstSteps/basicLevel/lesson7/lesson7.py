# exemplos de aula
nome = 'Davi'
idade = 21
peso = 102
altura = 1.84
maiorIdade = idade > 18
boolean = True #booleano só se escreve com letra maiúscula
imc = peso / (altura * altura)
#imc = peso / altura **2

print("nome:", nome)
print("idade:", idade)
print("altura:", altura)
print("maiorIdade:", maiorIdade)
print("boolean:", boolean)

print(nome, 'tem', idade, 'anos de idade, seu peso é de', peso, 'e seu imc é de', imc)
print(f"{nome} tem {idade} anos e atualmente está pesando {peso} e seu imc é de {imc:.2f}")
print('{} <- nome {} <- idade {} <- peso {:.2f} <- imc'.format(nome, idade, peso, imc))
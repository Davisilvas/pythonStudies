# Uma variável de classe pode ser acessada por qualquer instância ou diretamente pela classe. Mas não pode ser alterada pela instância.

#primeiro o python busca na instância. Se ele não achar na instância ele busca na classe e exibe o valor da classe.

# então se fizermos o seguinte

# a1 = A()
# ai.variavel_de_classe = 231
# print(a1.variavel_de_classe)
# print(A.variavel_de_classe)

# vamos ter 231 e embaixo 123 pois na linha 8 a gente acaba criando aquela variável na instancia, e não consumindo a variável da classe



class A:
    variavel_de_classe = 123 

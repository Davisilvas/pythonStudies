"""
Como criar nossos próprios pacotes.
"""
# import vendas.calcPreco

from vendas import calcPreco
from vendas.formata import preco

valor = 49.99
valorComAumento = calcPreco.aumento(valor, 10, True)
valorComDesc = calcPreco.desconto(valor, 50, True)

print(valorComAumento)
print(valorComDesc)
print(preco.real(75.98))

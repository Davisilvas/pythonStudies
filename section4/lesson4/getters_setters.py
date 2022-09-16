import produto

produto1 = produto.Produto('Coca-Cola 2Lt', 9.50)
produto1.desconto(30)
print(produto1.preco)

produto2 = produto.Produto('Coca-Cola 2Lt', 'R$55.50')
produto2.desconto(30)
print(produto2.preco)

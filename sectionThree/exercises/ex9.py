carrinho = []

carrinho.append(('produto 1', 12))
carrinho.append(('produto 2', 32))
carrinho.append(('produto 3', 22))

total = sum([float(y) for x, y in carrinho])

print(total)
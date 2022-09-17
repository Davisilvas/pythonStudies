import classe

bd = classe.BaseDeDados()
bd.inserir_cliente(1, 'Davi')
bd.inserir_cliente(2, 'Maria')
bd.inserir_cliente(3, 'Doly')

# print(bd.dados)
bd.listar_clientes()
bd.apagar_cliente(3)

# bd.listar_clientes()

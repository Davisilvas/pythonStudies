try:
    file = open('abc2.txt', 'w+')
    file.write('Vasco da Gama\n')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()

########### MELHOR FORMA DE ABRIR ARQUIVOS #################
# gerenciadores de contexto
# com o gerenciador de contexto a gente não precisa mandar fechar o arquivo. Com o With, ele mesmo já fecha o arquivo pra gente assim que acabar a execução.

# With + nome do arquivo a ser abert + as + variável que vamos usar para manipular o arquivo
with open('abc3.txt', 'w+') as file:
    file.write('Vasco\n')
    file.write('da\n')
    file.write('Gama\n')

    file.seek(0)
    print(file.read())

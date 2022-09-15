import dados

zipado_1 = list(zip(dados.cnpj1_p1, dados.cnpj_1v))

x = sum(dados.mult_phase1(zipado_1))

primeiro_digito = dados.formula(x)
dados.cnpj1_p2.append(primeiro_digito)

zipado_2 = list(zip(dados.cnpj1_p2, dados.cnpj_2v))

z = sum(dados.mult_phase2(zipado_2))

segundo_digito = dados.formula(z)

cnpj1_p3 = dados.cnpj1_p2.copy()
cnpj1_p3.append(segundo_digito)
# print(cnpj1_p3)

if dados.cnpj1_original == cnpj1_p3:
    print('CNPJ VALIDADÍSSIMO')
else:
    print('INVÁLIDO')

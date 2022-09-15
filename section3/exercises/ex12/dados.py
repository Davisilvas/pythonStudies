# 04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

# def remover_caracteres(cnpj):
#     cnpj = cnpj.replace('/', '')
#     cnpj = cnpj.replace('.','')
#     cnpj = cnpj.replace('-','')
#     return cnpj

def mult_phase1(zipp):
    new_list = []
    for i, v in zipp:
        r = (i * v)
        new_list.append(r)
    return new_list


def mult_phase2(zipp):
    new_list_phase2 = []
    for i, v in zipp:
        r = (i * v)
        new_list_phase2.append(r)
    return new_list_phase2


def formula(x):
    calc = 11 - (x % 11)
    if calc <= 9:
        return calc
    else:
        return 0


# ORIGINAIS PARA VALIDAÇÃO
cnpj1_original = [0, 4, 2, 5, 2, 0, 1, 1, 0, 0, 0, 1, 1, 0]
cnpj2_original = [4, 0, 6, 8, 8, 1, 3, 4, 0, 0, 0, 1, 6, 1]
cnpj3_original = [7, 1, 5, 0, 6, 1, 6, 8, 0, 0, 0, 1, 1, 1]
cnpj4_original = [1, 2, 5, 4, 4, 9, 9, 2, 0, 0, 0, 1, 0, 5]

cnpj_1v = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
cnpj_2v = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

# PRIMEIRO CNPJ 
cnpj1_p1 = [0, 4, 2, 5, 2, 0, 1, 1, 0, 0, 0, 1]
cnpj1_p2 = [0, 4, 2, 5, 2, 0, 1, 1, 0, 0, 0, 1]

# 4) Faça um programa com uma matriz com 9 elementos (3x3) reais positivos 
# (aleatórios e de sua escolha). Calcule e exiba a soma dos elementos de cada
# linha desta matriz.

# criando uma matriz 3x3 e preenchendo com os valores 
matriz1 = ([[1, 2, 3],
            [5, 6, 7],
            [8, 9, 10]
            ])

# fazendo a soma de cada elemento das linhas e armazenando em variáveis
# após isso, mostrará na tela o resultado de cada soma
soma0 = matriz1[0][0] + matriz1[0][1] + matriz1[0][2]
soma1 = matriz1[1][0] + matriz1[1][1] + matriz1[1][2]
soma2 = matriz1[2][0] + matriz1[2][1] + matriz1[2][2]
print("Soma da linha 1: {}\n".format(soma0))
print("Soma da linha 1: {}\n".format(soma1))
print("Soma da linha 1: {}\n".format(soma2))

    
# resultado
# Soma da linha 1: 6
# Soma da linha 1: 18
# Soma da linha 1: 27
# 2) Crie uma matriz de caracteres (char) de 16 posições (4x4). 
# Preencha-a com os valores a, b, c, d, e, f, g, h, i, j, k, l, m, n, o e p. 
# Use dois for para exibir os valores desta matriz.

# criando uma matriz 4x4 e preenchendo com os valores descritos no problema
matriz1 = ([['a', 'b', 'c', 'd'],
            ['e', 'f', 'g', 'h'],
            ['i', 'j', 'k', 'l'],
            ['m', 'n', 'o', 'p'],
            ])

# fazendo o i passar pelas colunas da matriz e o j pelas linhas,
# mostrando na tela as coordenadas do valor e o próprio valor
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        print("[{},{}]: {}\n".format(i, j, matriz1[i][j]))
    
# resultado
# [0,0]: a
# [0,1]: b
# [0,2]: c
# [0,3]: d
# [1,0]: e
# [1,1]: f
# [1,2]: g
# [1,3]: h
# [2,0]: i
# [2,1]: j
# [2,2]: k
# [2,3]: l
# [3,0]: m
# [3,1]: n
# [3,2]: o
# [3,3]: p
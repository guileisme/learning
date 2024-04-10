# 5) Faça um programa com uma matriz 5x5 de inteiros positivos ou negativos 
# (aleatórios e de sua escolha) e encontre e exiba o maior elemento desta matriz

matriz1 = ([[1, 2, 3, 400, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 1400, 15]
            ])

numerosMaximos = []
for i in range(len(matriz1)):
        numerosMaximos.append(max(matriz1[i]))
    
print("O maior número dentro da matriz é {}".format(max(numerosMaximos)))

# resultado
# O maior númeor dentro da matriz é 1400
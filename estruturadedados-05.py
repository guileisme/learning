# 5) Faça um programa com uma matriz 5x5 de inteiros positivos ou negativos 
# (aleatórios e de sua escolha) e encontre e exiba o maior elemento desta matriz

matriz1 = ([[1, 2, 3, 400, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15]
            ])

numerosMaximos = []
for i in range(len(matriz1)):
        numerosMaximos.append(max(matriz1[i]))
    
print(max(numerosMaximos))

# resultado
# 0: 10
# 1: 20
# 2: 30
# 3: 40
# 4: 50
# 5: 60
# 6: 70
# 7: 80
# 8: 90
# 9: 100
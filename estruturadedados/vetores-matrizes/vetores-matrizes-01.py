# 1) Crie um vetor de inteiros (int) de 10 posições. 
# Preencha-o com os valores 10, 20, 30, 40, 50, 60, 70, 80, 90 e 100. 
# Use um for para exibir os valores deste vetor.

# criando um vetor através de uma lista em python
vetor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# fazendo o i passar pelo vetor (lista) usando um for
# e mostrando na tela o índice do valor e o próprio valor
for i in range(len(vetor1)):
    print("{}: {}\n".format(i, vetor1[i]))
    
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
# 3) Faça um programa com um vetor com 10 elementos inteiros positivos 
# (aleatórios e de sua escolha). Permita que seja solicitado um determinado 
# valor inteiro e positivo para ser procurado neste vetor. Caso exista, 
# o programa deve exibir o índice no qual o valor está posicionado. 
# Caso contrário, o programa deve informar que o elemento não existe no vetor.

# criando um vetor através de uma lista em python e um input para o usuário
vetor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numero = int(input("Digite um número: "))

# criando uma variável para saber se o número existe dentro do vetor
# se ele existe, a variável é True e caso não, a variável é False
existe = False

# fazendo o i passar pelo vetor (lista) usando um for
# e comparando com o número digitado pelo usuário no input anterior
# caso o número esteja dentro do vetor, aparecerá na tela que ele está na lista
# junto de seu índice indicado. Além disso, a variável existe será True
for i in range(len(vetor1)):
    if numero == vetor1[i]:
        print("O número está na lista e o seu índice é {}".format(i))
        existe = True

# caso a variável seja False, aparecerá na tela uma mensagem mostrando que o
# número digitado pelo usuário não se encontra dentro do vetor
if existe != True:
    print("O número não está dentro do vetor.")
    
# resultado com o número estando no vetor
# Digite um número: 20
# O número está na lista e o seu índice é 1

# resultado com o número não estando no vetor
# Digite um número: 101
# O número não está dentro do vetor.
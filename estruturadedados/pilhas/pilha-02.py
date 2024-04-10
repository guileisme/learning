# 2) Um palíndromo é uma palavra, frase ou número pode ser lido de forma 
# igual em ambos os sentidos:  da direita para a esquerda e da esquerda 
# para a direita. Ex.: arara, 2002, "anotaram a data da maratona". 
# Crie um programa em C que verifica se uma palavra, frase ou número 
# é um palíndromo.

def palindromo(palavra):
    str(palavra)
    correto = False
    pilha = []
    for i in range(len(palavra)):
        pilha.append(palavra[(len(palavra)-1)-i])
    if len(palavra) == len(pilha):
        for i in range(len(palavra)):
            if palavra[i] == pilha[i]:
                correto = True
    if correto != True:
        print("Esta palavra não é um palíndromo!")
    else:
        print("Esta palavra é um palíndromo.")
    
palavra = str(input("Digite uma palavra ou frase e descubra se ela é um palíndromo: "))
palindromo(palavra)

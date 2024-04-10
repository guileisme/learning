# 4) Este é um desafio. Considere uma pilha contendo os seguintes 
# caracteres e nesta sequência de empilhamento: @, &, @, #, %, &, $. 
# Faça um programa que use pilhas para eliminar os caracteres repetidos.

pilha = ['@', '&', '@', '#', '%', '&', '$']

def eliminarRepetidos (pilha):
    pilhaAuxiliar1 = []
    pilhaAuxiliar2 = []
    i = 0
    pilhaAuxiliar1.append(pilha[i])
    while pilha != []:
        if pilhaAuxiliar1[i] != pilha[i]:
            pilhaAuxiliar1.append(pilha[i])
            del(pilha[i])
        else:
            del(pilha[i])
    i += 1
    pilhaAuxiliar2.append(pilhaAuxiliar1[i])
    while pilhaAuxiliar1 != []:
        if pilhaAuxiliar2[i-1] != pilhaAuxiliar1[i-1]:
            pilhaAuxiliar2.append(pilhaAuxiliar1[i-1])
            del(pilhaAuxiliar1[i-1])
        else:
            del(pilhaAuxiliar1[i-1])

    return print(pilhaAuxiliar2)
    
eliminarRepetidos(pilha)

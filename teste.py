import numpy as np

matriz_1 = np.array([
    [2,4,5],
    [5,6,8],
])

def calculaMedia (matriz):
    soma = matriz.sum(axis = 1)
    media = soma/len(matriz)
    print("A média da matriz é: " + media)

calculaMedia(matriz_1)








    


    
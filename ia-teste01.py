# importando bibliotecas recomendadas pelo professor

# numpy está sendo usado para criar a imagem e pintar os pontos 
import numpy as np

#
import matplotlib.pyplot as plt

#
import cv2

#
import time
# from google.colab.patches import cv2_imshow

# funções

# função para pintar no mapa criado 
def pintar(x, y, R, G, B, imagem):
    mapa = imagem
    mapa[x,y] = (B, G, R)
    return mapa

# função para mostrar o mapa criado 
def mostrar(mapa):
    cv2.imshow('image',mapa)
    cv2.waitKey(0)

# função para criar a fronteira dos dados
def fronteira ():
    

# criando o mapa
imagem = np.zeros((50,50, 3), dtype="uint8")

# definindo a posição inicial e pintando de verde
pontoInicial = pintar(0,0,0,255,0,imagem)
posicaoInicial = [0,0]

# definindo a posição final e pintando de azul
pontoFinal = pintar(8,6,0,0,255,imagem)
posicaoFinal = [8,6]

# definindo as posições dos obstáculos
obstaculo1 = [4,4]
obstaculo2 = [4,5]
obstaculo3 = [4,6]
obstaculo4 = [4,7]
obstaculo5 = [4,8]
obstaculo6 = [5,8]
obstaculo7 = [6,8]
obstaculo8 = [7,8]

# pintando os obstáculos de branco
pintar(4, 4, 255, 255, 255, imagem)
pintar(4, 5, 255, 255, 255, imagem)
pintar(4, 6, 255, 255, 255, imagem)
pintar(4, 7, 255, 255, 255, imagem)
pintar(4, 8, 255, 255, 255, imagem)
pintar(5, 8, 255, 255, 255, imagem)
pintar(6, 8, 255, 255, 255, imagem)
pintar(7, 8, 255, 255, 255, imagem)

# fronteira de dados e os passos que são necessários para chegar até o ponto
fronteira = []
passos = 0

# aumentando a resolução para que a imagem não fique borrada e muito pequena na tela
resolucao = cv2.resize(imagem, dsize=(300, 300), interpolation=cv2.INTER_NEAREST_EXACT)

mostrar(resolucao)

# while posicaoInicial[0] != posicaoFinal[0]:
#     posicaoInicial[0] += 1
#     pontoInicial = pintar(posicaoInicial[0],posicaoInicial[1],255,0,0,imagem)
#     resolucao = cv2.resize(imagem, dsize=(300, 300), interpolation=cv2.INTER_NEAREST_EXACT)
#     mostrar(resolucao)

#     while posicaoInicial[1] != posicaoFinal[1]:
#         posicaoInicial[1] += 1
#         pontoInicial = pintar(posicaoInicial[0],posicaoInicial[1],255,0,0,imagem)
#         resolucao = cv2.resize(imagem, dsize=(300, 300), interpolation=cv2.INTER_NEAREST_EXACT)
#         mostrar(resolucao)

while posicaoInicial != posicaoFinal:
    passos += 1
    fronteira.append(passos)

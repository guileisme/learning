# importando bibliotecas recomendadas pelo professor

# numpy está sendo usado para criar a imagem e pintar os pontos 
import numpy as np

# coloquei aqui porque foi uma biblioteca que o professor
# estava usando e talvez possa vir a ser útil
import matplotlib.pyplot as plt

# cv2 está sendo usada para mostrar as imagens em uma janela
import cv2

# o colab não deve conseguir abrir uma janela, então é preciso
# importar essa biblioteca de patches para fazer o cv2 funcionar
# from google.colab.patches import cv2_imshow

movimento = [[0,1], [0,-1], [1,0], [-1,0]]
custoMovimento = 1

def __init__(self, posicao, custo):
    self = {posicao : custo}

# FUNÇÕES:
# função para pintar no mapa criado 
def pintar(x, y, R, G, B, imagem):
    mapa = imagem
    mapa[x,y] = (B, G, R)
    return mapa

# função para mostrar o mapa criado 
def mostrar(mapa):
    cv2.imshow('image',mapa)
    cv2.waitKey(0)

def CustoUniforme(posicaoInicial, posicaoFinal, mapa):
    fronteira = []
    fronteira.append(posicaoInicial)
    visitados = []
    visitei = []

    while fronteira:
        posicaoAtual = fronteira.pop()
        visitados.append(posicaoAtual)

        if posicaoAtual == posicaoFinal:
            return visitei
        
        for i in movimento:
            posicaoProxima = (posicaoAtual[0] + i[0], posicaoAtual[1], i[1])
            if posicaoProxima != obstaculos[0] and posicaoProxima != obstaculos[1] and posicaoProxima != obstaculos[2] and posicaoProxima != obstaculos[3] and posicaoProxima != obstaculos[4] and posicaoProxima != obstaculos[5] and posicaoProxima != obstaculos[6] and posicaoProxima != obstaculos[7] and posicaoProxima not in visitados:
                custoProximo += posicaoAtual[custo] + custoMovimento
                vizinho = vizinho(posicaoProxima, custoProximo)
                fronteira.append(vizinho)
                visitei.append(posicaoProxima)

    return None

def melhorPrimeiro(pocicaoInicial, posicaoFinal, mapa):
    fronteira = []

def aEstrela(pocicaoInicial, posicaoFinal, mapa):
    fronteira = []

# criando o mapa
imagem = np.zeros((50,50, 3), dtype="uint8")

# definindo a posição inicial e pintando de verde
pontoInicial = pintar(0,0,0,255,0,imagem)
posicaoInicial = [0,0]

# definindo a posição final e pintando de azul
pontoFinal = pintar(8,6,0,0,255,imagem)
posicaoFinal = [8,6]

# definindo as posições dos obstáculos
obstaculos =[  [4,4], [4,5], [4,6], [4,7], [4,8],
                [5,8], [6,8], [7,8]
            ]

# pintando os obstáculos de branco
pintar(4, 4, 255, 255, 255, imagem)
pintar(4, 5, 255, 255, 255, imagem)
pintar(4, 6, 255, 255, 255, imagem)
pintar(4, 7, 255, 255, 255, imagem)
pintar(4, 8, 255, 255, 255, imagem)
pintar(5, 8, 255, 255, 255, imagem)
pintar(6, 8, 255, 255, 255, imagem)
pintar(7, 8, 255, 255, 255, imagem)

# aumentando a resolução para que a imagem não fique borrada e muito pequena na tela
resolucao = cv2.resize(imagem, dsize=(300, 300), interpolation=cv2.INTER_NEAREST_EXACT)
mostrar(resolucao)

# busca de custo uniforme
def buscaCustoUniforme():
    print("Busca de Custo Uniforme")
    custoUniforme = CustoUniforme(posicaoInicial, posicaoFinal, imagem)
    caminho = []
    posicaoAtual = posicaoFinal
    while posicaoInicial != posicaoFinal:
        caminho.append(posicaoAtual)
        posicaoAtual = custoUniforme[posicaoAtual]
        pintar(posicaoAtual[0], posicaoAtual[1], 255, 0, 0, imagem)
        resolucao = cv2.resize(imagem, dsize=(300, 300), interpolation=cv2.INTER_NEAREST_EXACT)
        mostrar(resolucao)
    caminho.append(posicaoInicial)
    caminho.reverse()

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

# while posicaoInicial != posicaoFinal:
#     passos += 1
#     fronteira.append(passos)

buscaCustoUniforme()
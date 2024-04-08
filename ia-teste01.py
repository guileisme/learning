import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
# from google.colab.patches import cv2_imshow

#funções
def pintar(x, y, R, G, B, imagem):
    mapa = imagem
    mapa[y,x] = (B, G, R)
    return mapa

def mostrar(mapa):
    cv2.imshow(mapa)

def calcDistancia (pontoInicialX, pontoInicialY, pontoFinalX, pontoFinalY):
    xDist = abs(pontoInicialX - pontoFinalX)   
    yDist = abs(pontoInicialY - pontoFinalY)   
    distancia = np.sqr(xDist**2 + yDist**2)
    return distancia

imagem = np.zeros((50,50, 3), dtype="uint8")
pontoInicial = pintar(0,0,0,255,0,imagem)
piX = 0
piY = 0
pontoFinal = pintar(8,6,0,0,255,imagem)
pfX = 8
pfY = 6
resolucao = cv2.resize(imagem, dsize=(300, 300), interpolation=cv2.INTER_NEAREST_EXACT)

mostrar(resolucao)

#distância entre ponto final e inicial

while calcDistancia(piX, piY, pfX, pfY) != 0:
    if (piX < pfX):
        piX += 1
    
    if (piX > pfX):
        piX -= 1
    
    if (piY < pfY):
        piX += 1
    
    if (piY > pfY):
        piX -= 1


while piX != pfX:
    if (piX < pfX):
        piX += 1
    
    if (piX > pfX):
        piX -= 1
    
    pontoInicial = pintar(piX,0,255,0,0,imagem)
    resolucao = cv2.resize(imagem, dsize=(300, 300), interpolation=cv2.INTER_NEAREST_EXACT)
    mostrar(resolucao)

while piY < pfY:
    piY += 1
    pontoInicial = pintar(piX,piY,255,0,0,imagem)
    resolucao = cv2.resize(imagem, dsize=(300, 300), interpolation=cv2.INTER_NEAREST_EXACT)
    mostrar(resolucao)



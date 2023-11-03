# PROBLEMA-01
# def function(x):
# 	return x**2-2

# a = int(input("Digite um ponto a: "))
# b = int(input("Digite um ponto b: "))

# for i in range(a,b):
#     function(i)
#     if function(i)*function(i+1) < 0:
#         print("Existe um zero no intervalo [{}, {}]".format(a,b))
#     else:
#         print("Não existe um zero no intervalo [{}, {}]".format(a,b))

# PROBLEMA-02
# def function(x):
#     return x**2-2

# a = float(input("Digite um ponto a: "))
# b = float(input("Digite um ponto b: "))
# xMedio = 0

# while b-a>10**-15:
#     xMedio = (a + b)/2
#     if function(a)*function(xMedio) <0:
#         b = xMedio
#     else:
#         a = xMedio

# print(xMedio)

# PROBLEMA-03
# def function (x):
#     return x**2-2

# a = float(input("Digite um ponto a: "))
# b = float(input("Digite um ponto b: "))
# xMedio = 0

# while b-a>10**-10 & abs(function(x))>10**-3:
#     xMedio = (a*function(b) - b*function(a))/(function(b) - function(a))
#     if function(a)*function(xMedio)<0:
#         b = xMedio
#     else:
#         a = xMedio

# print(xMedio)

# PROBLEMA-04
# def function (x):
#     return x**2-2

# def derivative(x):
#     return 2*x

# x0 = 1.5

# for i in range (1,100):
#     xK = x0 - function(x0)/derivative(x0)

# print (xK)

# ALGORITMO DE EUDOXO
print("Esse programa vai calcular qualquer raiz quadrada que você quiser.")
n = int(input("Digite a raiz quadrada que você quer calcular: "))
def function(y):
    # if y<0:
    #     return print("A raiz quadrada é inválida.")
    return y**2 - n

# a = int(input("Defina o ponto inicial do intervalo: "))
# b = int(input("Defina o ponto final do intervalo: "))
xMedio = 0

# while function(a)*function(b) > 0:
#     if function(a) or function(b) == "A raiz quadrada é inválida.":
#         print("Raiz quadrada inválida.")
#     print("Não existe um zero no intervalo [{}, {}]. Por favor, digite um intervalo válido".format(a,b))
#     a = int(input("Defina o ponto inicial do intervalo: "))
#     b = int(input("Defina o ponto final do intervalo: "))

a = 0
b = 100000
# print("Existe um zero no intervalo [{}, {}]".format(a,b))

while b-a>10**-15:
    xMedio = (a + b)/2
    if function(a)*function(xMedio) <0:
        b = xMedio
    else:
        a = xMedio

xMedio = round(xMedio, 5)
print("A raiz quadrada de {} é {}.".format(n, xMedio))
input()
        
    



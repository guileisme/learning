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

    
        
    



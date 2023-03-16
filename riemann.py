import numpy as np

input("Este programa vai calcular a área do gráfico da função f(x)=x² em um certo intervalo.")

def func (x):
    y = x**2
    return y

a = int(input("Defina o início do intervalo: "))
b = int(input("Defina o final do intervalo: "))
n = float(input("Defina a base dos retângulos: "))

lista_func = []

x = np.arange(a,b,n)

for i in x:
    lista_func.append(func(i)*n)

soma = sum(lista_func)

print(soma)







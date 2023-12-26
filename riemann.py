import numpy as np

print("Este programa vai calcular a área do gráfico da função f(x)=x² em um certo intervalo.")

def func (x):
    y = x**2
    return y

a = int(input("Defina o início do intervalo: "))
b = int(input("Defina o final do intervalo: "))
n = int(input("Defina a base dos retângulos: "))
base = (b-a)/n
lista_func = []
x = np.arange(a,b,base)

for i in x:
    print(lista_func)
    lista_func.append((func(i)*n))


soma = sum(lista_func)

print(soma)

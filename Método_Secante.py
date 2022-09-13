from numpy import *
import math
import pandas as pd

print("MÉTODO DA SECANTE")
print('DIGITE AQUI OS VALORES PARA x0 E x1')
x = float(input('DIGITE O VALOR DE x0: '))
x1 = float(input('DIGITE O VALOR DE x1: '))
er = eval(input('DIGITE O VALOR DO SEU ERRO: '))
y1 = input('ESCREVA A SUA FUNÇÃO f(x): ')


def f(x):
    y = eval(y1)
    return y

k=2
k1=[]
x3=[]
fxm=[]
k1.append(0)
k1.append(1)
x3.append(x)
x3.append(x1)
fxm.append(f(x))
fxm.append(f(x1))
while abs(f(x1))>er:
    x2 = x1 - (f(x1)*(x1-x))/(f(x1)-f(x))
    k1.append(k)
    x3.append(x2)
    fxm.append(f(x2))
    x=x1
    x1=x2
    k=k+1

k2=k-1

df= pd.DataFrame(data={'ITERAÇÕES':k1,'x':x3,'f(x)':fxm})
print(df.to_string(index=False))
print('A RAIZ PARA A FUNÇÃO',y1, 'É APROX. x= ',x1, 'COM',k2,'ITERAÇÕES')
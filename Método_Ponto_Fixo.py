from numpy import*
import math
import pandas as pd

print("MÉTODO DO PONTO FIXO")
print("INFORME OS VALORES INICIAS DE a E b")
a=int(input("DIGITE O VALOR DE a: "))
b=int(input("DIGITE O VALOR DE b: "))
er=float(input("DIGITE O VALOR DO ERRO: "))
y1=input("DIGITE AQUI A SUA FUNÇÃO PRINCIPAL f(x): ")
y2=input("DIGITE AQUI A SUA FUNÇÃO AUXILIAR g(x): ")

def f(x):
    y=eval(y1)
    return y

def g(x):
    z=eval(y2)
    return z
k1 = []   
x1 = []
fxm = []
gxm = []
X_m = (a+b)/2
k=1
k1.append(0)
x1.append(X_m)
fxm.append(f(X_m))
gxm.append(g(X_m))
while abs(f(X_m))>er:
    X_m = g(X_m)
    k1.append(k)
    x1.append(X_m)
    fxm.append(f(X_m))
    gxm.append(g(X_m))
    k=k+1
k2=k-1
df = pd.DataFrame(data={'ITERAÇÃO':k1,'X_m':x1,'f(X_m)':fxm,'g(X_m)':gxm})
print((df.to_string(index=False)))
print('A RAIZ PARA A EQUAÇÃO',y1,'É APROX. x=', X_m, 'COM', k2, 'ITERAÇÕES')
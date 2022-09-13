import pandas as pd
from numpy import*
import math


print("MÉTODO DA FALSA POSIÇÃO")

print("INSERI ASSEGUIR OS VALORES INCIAIS DO INTERVALO a E b")
a = int(input("DIGITE O VALOR DE a: "))
b = int(input("DIGITE O VALOR DE b: "))
er = float(input("DIGITE AQUI O VALOR DO ERRO EM DECIMAL: "))
arre = int(input("DIGITE AQUI O ARREDONDAMENTO DA RAÍZ: "))
y1 = (input("DIGITA A AQUI A SUA EQUAÇÃO: "))


def f(x):
    y = eval(y1)
    return y
k1=[]
a1 = []
b1 = []
x1 = []
fa = []
fb = []
fxm = []
err2 = []    

X_m=(a*f(b)-b*f(a))/(f(b)-f(a))
k=0
er1=b-a

while abs(f(X_m))>er:
    X_m=(a*f(b)-b*f(a))/(f(b)-f(a))
    er1=b-a
    k1.append(k)
    a1.append(a)
    b1.append(b)
    x1.append(X_m)
    fa.append(f(a))
    fb.append(f(b))
    fxm.append(f(X_m))
    err2.append(er1)
    if (f(a)*f(X_m))<0:
        a=a
        b=X_m
    elif (f(X_m)*f(b))<0:
        a=X_m
        b=b
    k=k+1
    

df = pd.DataFrame(data={'ITERAÇÃO':k1,'a':a1,'b':b1,'X_m':x1,'f(a)':fa,'f(b)':fb,'f(X_m)':fxm,'ERRO':err2})
print((df.to_string(index=False)))
print('A RAÍZ PARA A EQUAÇÃO',y1,'É APROX. x=', round(X_m,arre), 'COM', k, 'ITERAÇÕES')
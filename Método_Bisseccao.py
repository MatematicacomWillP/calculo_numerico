import pandas as pd
from numpy import*
import math

print("MÉTODO DA BISSECÇÃO")

print("INSERI ASSEGUIR OS VALORES INCIAIS DO INTERVALO a E b")
a = int(input("DIGITE O VALOR DE a: "))
b = int(input("DIGITE O VALOR DE b: "))
er = float(input("DIGITE AQUI O VALOR DO ERRO EM DECIMAL: "))
k = int(math.ceil((math.log10(b-a) - (math.log10(er)))/math.log10(2)))
print("NÚMERO DE ITERAÇÕES, SERÁ IGUAL k=",k)
y1 = (input("DIGITA A AQUI A SUA EQUAÇÃO: "))

def f(x):
    y = eval(y1)
    return y
k1 = []   
a1 = []
b1 = []
x1 = []
fa = []
fb = []
fxm = []
err2 = []
for i in range(0,k+1):
    X_m = (a+b)/2
    er1=b-a
    k1.append(i)
    a1.append(a)
    b1.append(b)
    x1.append(X_m)
    fa.append(f(a))
    fb.append(f(b))
    fxm.append(f(X_m))
    err2.append(er1)
    if f(a)*f(X_m)<0:
        b=X_m
    else:
        a=X_m
    

df = pd.DataFrame(data={'ITERAÇÃO':k1,'a':a1,'b':b1,'X_m':x1,'f(a)':fa,'f(b)':fb,'f(X_m)':fxm,'ERRO':err2})
print((df.to_string(index=False)))
print('A RAÍZ PARA A EQUAÇÃO',y1,'É APROX. x= ', round(X_m,2))
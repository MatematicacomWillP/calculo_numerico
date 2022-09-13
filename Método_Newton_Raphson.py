from numpy import*
import math
import pandas as pd 


print("MÉTODO DE NEWTON-RAPSHON")
valor=int(input("DIGITE [1] SE FOR USAR UM INTERVALO OU [2] SE FOR USAR UM VALOR INICIAL: "))
if valor == 1:
    print("INFORME A SEGUIR OS VALORES DE a E b")
    a = int(input("DIGITE O VALOR DE a: "))
    b = int(input("DIGITE O VALOR DE b: "))
    x = (a + b)/2
elif valor == 2:
    vi = float(input("DIGITE O VALOR DE INICIAL DE x: "))
    x = vi
else:
    print("VALOR INVÁLIDO! REINICIE O PROGRAMA")
    exit()

er = eval((input("DIGITE O VALOR DO ERRO: ")))
y1 = input("DIGITE AQUI A SUA FUNÇÃO f(x): ")

def f(x):
    y = eval(y1)
    return y
def g(x):
    z=(f(x+er)-f(x))/er
    return z
    
k1 = []   
x1 = []
fxm = []
gxm = []
k1.append(0)
x1.append(x)
fxm.append(f(x))
gxm.append(g(x))
k = 1
while abs(f(x))>er:
    x = x - f(x)/g(x)
    k1.append(k)
    x1.append(x)
    fxm.append(f(x))
    gxm.append(g(x))
    k=k+1
k=k-1    

df = pd.DataFrame(data={'ITERAÇÃO':k1,'X_m':x1,'f(X_m)':fxm,'g(X_m)':gxm})
print((df.to_string(index=False)))
print('A RAIZ PARA A FUNÇÃO',y1,'É APROX. x=',x, 'COM',k, 'ITERAÇÕES')
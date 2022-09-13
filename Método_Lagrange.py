#== LAGRANGE ==#
from numpy import*
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('MÉTODO POLINOMIAL DE LAGRANGE')
itercao = int(input('ENTRE AQUI COM A QUATIDADE ELEMENTOS DA INTERPOLÇÃO: '))

x = []
+[]

for i in range(itercao):     
    for j in range(1):        
        x.append(float(input('DIGITE O VALOR DE x'+str(i)+': ')))
        y.append(float(input('DIGITE O VALOR DE y'+str(i)+': ')))     

var = float(input('DIGITE AGORA O VALOR DE P(x): '))
n = itercao-1
y1=0
k1 = []
for i in range(0,n+1):
    p=1
    k1.append(i)
    for j in range(0,n+1):
        if i != j:
            p = p*(var-x[j])/(x[i]-x[j])
    y1 = y1 + p * y[i]

df = pd.DataFrame(data={'i':k1,'x':x,'y':y})
print((df.to_string(index=False)))
print('P(%.3f) = %.3f ' %(var,y1))

plt.figure(num=0,dpi=120)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('$f(x)$')
plt.show()
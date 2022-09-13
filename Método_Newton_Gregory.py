#== NEWTON ==#
from numpy import*
import numpy as np
import pandas as pd
from math import*

print('MÉTODO POLINOMIAL DE NEWTON-GREGORY')
itercao = int(input('ENTRE AQUI COM A QUATIDADE ELEMENTOS DA INTERPOLÇÃO: '))

x = []
y = []

for i in range(itercao):     
    for j in range(1):        
        x.append(float(input('DIGITE O VALOR DE x'+str(i)+': ')))
        y.append(float(input('DIGITE O VALOR DE y'+str(i)+': ')))     

y1 = [[None for x in range(itercao)] for x in range(itercao)]
col = []
for i in range(itercao):
    y1[i][0] = y[i]
    col.append('Ordem '+str(i))

for j in range(1,itercao):
    for i in range(itercao-j):
        y1[i][j]=(y1[i+1][j-1]-y1[i][j-1])

#==PARA A CRIAÇÃO DA TABELA==#
df = pd.DataFrame(y1,index=x, columns=col)
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'x'})
print(((df.to_string(index=False))))

var = float(input('DIGITE AQUI O VALOR DE x: '))
#== valor de u ==#
u = (var - x[0])/(x[1] - x[0])
print('O valor de u= %f' %u)

def u_cal(u, itercao):
 
    temp = u
    for i in range(1, itercao):
        temp = temp * (u - i)
    return temp

yi = y1[0][0]
for i in range(1,itercao):
    yi = yi + (u_cal(u,i)*y1[0][i])/factorial(i)
print('O VALOR DE P(%f) = %f'%(var,yi))


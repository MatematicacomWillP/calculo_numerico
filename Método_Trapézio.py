from numpy import*
import math
import pandas as pd

print('INTEGRAÇÃO NUMÉRICA - TRAPÉZIO')
a = (input('DIGITE O VALOR DE a: '))
b = (input('DIGITE O VALOR DE b: '))
y1 = (input("DIGITA A AQUI A SUA EQUAÇÃO: "))

x = []
x.append(eval(a))
x.append(eval(b))

def f(x):
   y = eval(y1)
   return y
print('\nTRAPÉZIO SIMPLES\n')
def tsimples(x):
    h = x[1] - x[0]
    print('VALOR DO h = ',h)
    b = (f(x[0])+f(x[1]))/2
    y = b*h
    return y

print('TRAPÉZIO SIMPLES = ', tsimples(x))

print('\nTRAPÉZIO REPETIDA\n')
n = int(input('VALOR DOS SUBINTERVALOS: '))
h = (x[1] - x[0])/n
x1 = []
soma = x[0]
x1.append(soma)
for i in range(1,n+1):
    soma = soma + h
    x1.append(soma)
print('VALOR DO h = ',h)

y2 = []
for i in x1[0:n+1]:
    soma1 = f(i)
    y2.append(soma1)

p = []
y3 = []
p.append(1)
y3.append(y2[0]) 
for i in range(1,n):
    p.append(2)
p.append(1)

for i in y2[1:n]:
    mult = 2*i
    y3.append(mult)
y3.append(y2[n]) 

def trepetida(x):
    soma2 = y3[0] + y3 [n]
    for i in y3[1:n]:
        soma2 = soma2 + i
    y = soma2*(h/2)
    return y

df = pd.DataFrame(data={'xi':x1,'f(xi)':y2,'p':p,'p*f(xi)':y3})
print(df)
print('TRAPÉZIO REPEDIDA = ',trepetida(x))

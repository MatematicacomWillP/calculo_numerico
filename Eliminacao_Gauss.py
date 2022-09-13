from numpy import *
import numpy as np

print('RESOLUÇÃO DE SISTEMA LINEAR PELA ELIMINAÇÃO DE GAUSS')

#MATRIZ PRINCIPAL, OU SEJA A MATRIZ A#

L = int(input('QUAL É O TAMANHO DE SUA MATRIZ: '))
M = [[0] * L for i in range(L)]
for i in range(L):      
    for j in range(L):        
        M[i][j]=float(input('ELEMENTO ['+str(i+1)+']''['+str(j+1)+']: ' ))       
f = np.array(matrix(M))

#MATRIZ DOS ELEMENTOS DAS IGUALDADES DE A SENDO APENAS O NÚMERO DE LINHAS IGUAL O DIGITADO ACIMA E A COLUNA SEMPRE IGUAL 1, 
#POIS SE TRATA DE UM VETOR#

print('DIGITE DIGITE AGORA OS VALORES DA IGUALDADE, NO CASO OS VALORES DE b:')
C1 = 1
M1= [[0] * C1 for i in range(L)]
for i in range(L):      
    for j in range(C1):        
        M1[i][j]=float(input('ELEMENTO ['+str(i+1)+']''['+str(j+1)+']: ' ))       
f1 = np.array(matrix(M1))

M2= [[0] * C1 for i in range(L)]
for i in range(L):      
    for j in range(C1):        
        M2[i][j]= 'x'+ str(i+1)       
f2 = np.array(matrix(M2))

print('MATRIZ INICIAL:' '\n' 'MATRIZ A \t\t\t MATRIZ b' '\n' + "\n".join('{}\t{} = {}'.format(f,f2,f1) for f,f2,f1 in zip(f,f2,f1)))
print('')
print('REALIZANDO AS ELIMINAÇÕES')
print('')

for k in range(L-1):
    for i in range(k+1,L):
        m = f[i,k]/f[k,k]
        f[i,:]=f[i,:]-m*f[k,:]
        f1[i,:]=f1[i,:]-m*f1[k,:]
        print('Pivô = ',f[k,k])
        print('m = ',m)
        print('\n'.join('{}\t {} = {}'.format(f,f2,f1) for f,f2,f1 in zip(f,f2,f1)))
        print('')

print('RESOLVENDO O SISTEMA')
print('A SOLUÇÃO DO SISTEMA É: ')
x=zeros(L)
x[L-1] = f1[L-1]/f[L-1,L-1]
print('x'+str(L)+'=', x[L-1])
for i in range(L-2,-1,-1):
    sum_ax = 0
    for j in range(i+1,L):
        sum_ax += f[i,j]*x[j]
    x[i]=(f1[i]-sum_ax)/f[i,i]
    print('x'+str(i+1)+'=', x[i])

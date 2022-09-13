from numpy import*
import numpy as np 

print('RESOLUÇÃO DE SISTEMA LINEAR FATOR LU')

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

#MATRIZ IDENTIDADE#
M2=np.zeros((L,L))
for i in range(L):
    for j in range(L):
        if i==j:
            M2[i,j]=1
        if i<j:
            M2[i,j]=0
f2 = np.array(matrix(M2))


print('MATRIZ INICIAL:' '\n' 'MATRIZ U \t MATRIZ b \t MATRIZ L' '\n' + "\n".join('{}\t{} {}'.format(f,f1,f2) for f,f1,f2 in zip(f,f1,f2)))
print('')
print('REALIZANDO AS ELIMINAÇÕES')
print('')

for k in range(L-1):
    for i in range(k+1,L):
        m= f[i,k]/f[k,k]
        f[i,:]=f[i,:]-m*f[k,:]
        if k<i:
            f2[i,k]=m
        print('pivô =', f[k,k])
        print('m = ',m)
        print( "\n".join('{}\t{} {}'.format(f,f1,f2) for f,f1,f2 in zip(f,f1,f2)))
print('')
print('RESOLVENDO OS SISTEMAS')
print('PARA O SISTEMA L')

y=np.zeros(L)
y[L-3]=f1[L-3]/f2[L-3,L-3]
print('y'+str(1)+'=',y[L-3])
for i in range(1,L):
    soma=0
    for j in range(0,L):
        soma += f2[i,j]*y[j]
    y[i]=(f1[i]-soma)/f2[i,i]
    print('y'+str(i+1)+'=',y[i])

print('PARA O SISTEMA U')

x=np.zeros(L)
x[L-1]=y[L-1]/f[L-1,L-1]
print('x'+str(L)+'=',x[L-1])
for i in range(L-2,-1,-1):
    soma=0
    for j in range(i+1,L):
        soma += f[i,j]*x[j]
    x[i]=(y[i]-soma)/f[i,i]
    print('x'+str(i+1)+'=',x[i])
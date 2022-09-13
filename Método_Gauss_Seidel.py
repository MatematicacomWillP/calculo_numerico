#== MÉTODO DE GAUSS-SEIDEL ==#
from numpy import*
import numpy as np

#== INICIO DA CONSTRUÇÕES DAS MATRIZES ==#

print('MÉTODO DE GAUSS-SEIDEL')
L=int(input('DIGITE AQUI O TAMANHO DE SUA MATRIZ: '))

M = [[0] * L for i in range(L)]
for i in range(L):      
    for j in range(L):        
        M[i][j]=float(input('ELEMENTO ['+str(i+1)+']''['+str(j+1)+']: ' ))       
f = np.array(M)

print('DIGITE DIGITE AGORA OS VALORES DA IGUALDADE, NO CASO OS VALORES DE b:')
C1 = 1
M1= [[0] * C1 for i in range(L)]
for i in range(L):      
    for j in range(C1):        
        M1[i][j]=float(input('ELEMENTO ['+str(i+1)+']''['+str(j+1)+']: ' ))      
f1 = np.array(M1)

M2= [[0] * C1 for i in range(L)]
for i in range(L):      
    for j in range(C1):        
        M2[i][j]= 'x'+ str(i+1)+'^(k)'      
f2 = np.array(M2)

M3= [[0] * C1 for i in range(L)]
for i in range(L):      
    for j in range(C1):        
        M3[i][j]= 'x'+ str(i+1) +'^(k+1)'       
f3 = np.array(M3)

print('MATRIZ INICIAL:' '\n' + "\n".join('{} = {}'.format(f,f1) for f,f1 in zip(f,f1)))

nova = np.zeros((L,L))
nova1 = np.zeros(L)
M4= [[0] * C1 for i in range(L)]
for i in range(0,L):
    nova[i:]= - f[i,:]/f[i,i]
    M4[i] = f1[i]/f[i,i]
    nova[i,i] = 0 
f4 = np.array(M4)
print('MATRIZ DAS ITERAÇÕES:' '\n' + "\n".join('{} = {} {} + {}'.format(f3,nova,f2,f4) for f3,nova,f2,f4 in zip(f3,nova,f2,f4)))

#== FIM DA CONSTRUÇÕES DAS MATRIZES ==#

print('AGORA INDIQUE QUAL SERÁ SEU CRITÉRIO DE PARADA')
opcao=int(input('DIGITE [1] SE FOR COM ITERAÇÕES OU [2] SE FOR COM O ERRO: '))
if opcao == 1:

    maxitera = int(input('ENTRE AQUI COM A QUATIDADE DE ITERAÇÕES: '))
    a = int(input('DIGITE AQUI O VALOR DAS CASAS DECIMAIS: '))
    print('VALORES INICIAIS PARA x')
    xi = np.zeros((L,1))
    for i in range(L):
        xi[i]=float(input('x'+str(i+1)+'^(0) = ' ))
    print('0',xi.T,'****') 
    #== CALCULANDO O PRIMEIRO ERRO ==#
    xkc = f4
    erro = (max(abs(xkc-xi))/max(abs(xkc)))[0]
    itera = 0
    xk = np.zeros((L,1))
    while itera < maxitera:
        itera = itera + 1
        f4 = xk.copy()
        xkc = xk.copy()
        for i in range(1,L+1,1):
            soma1 = 0
            for j in range(1,L+1,1):
                if ((i-1) > (j-1)):
                    soma1 = soma1 + f[i-1][j-1]*xk[j-1]     
                elif ((i-1) < (j-1)):
                    soma1 = soma1 + f[i-1][j-1]*f4[j-1]    
            xk[i-1] = (1/f[i-1,i-1])*(f1[i-1]-soma1)  
        erro = (max(abs(xk-xkc))/max(abs(xk)))[0]    
        print(itera, np.around(xk.T,a), erro)
if opcao == 2:
    er = eval(input('DIGITE AQUI O VALOR DA PRECISSÃO: '))
    a = int(input('DIGITE AQUI O VALOR DAS CASAS DECIMAIS: '))
    print('VALORES INICIAIS PARA x')
    xi = np.zeros((L,1))
    for i in range(L):
        xi[i]=float(input('x'+str(i+1)+'^(0) = ' ))
    print('0',xi.T,'****') 
    #== CALCULANDO O PRIMEIRO ERRO ==#
    xkc = f4
    erro = (max(abs(xkc-xi))/max(abs(xkc)))[0]
    itera = 0
    xk = np.zeros((L,1))
    while erro > er:
        itera = itera + 1
        f4 = xk.copy()
        xkc = xk.copy()
        for i in range(1,L+1,1):
            soma1 = 0
            for j in range(1,L+1,1):
                if ((i-1) > (j-1)):
                    soma1 = soma1 + f[i-1][j-1]*xk[j-1]     
                elif ((i-1) < (j-1)):
                    soma1 = soma1 + f[i-1][j-1]*f4[j-1]    
            xk[i-1] = (1/f[i-1,i-1])*(f1[i-1]-soma1)  
        erro = (max(abs(xk-xkc))/max(abs(xk)))[0]    
        print(itera, np.around(xk.T,a), erro)    
else:
    exit()
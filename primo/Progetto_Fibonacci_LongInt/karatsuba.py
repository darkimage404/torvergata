'''
Created on 27/gen/2015

@author: Francesco

'''

def karatsuba(a,b):
    mol1=str(a)
    mol2=str(b)
    len1=len(mol1)
    len2=len(mol2)
    lenght=sameLen(mol1,mol2,len1,len2)
    return recMolt(int(mol1),int(mol2),lenght)
    
def sameLen(a,b,len1,len2):    
    if len1>len2:
        return len1
    else:
        return len2

def recMolt(a,b,lent):
    if lent==1:
        return a*b
    else:
        x0=a%(10**(lent/2))
        x1=a/(10**(lent/2))
        y1=b/(10**(lent/2))
        y0=b%(10**(lent/2))
        x2=str(x1+x0)
        y2=str(y1+y0)
        lenx2=len(x2)
        leny2=len(y2)
        lenght=sameLen(x2,y2,lenx2,leny2)
        print a,b,'questi sono i valori da moltiplicare'
        print x1,x0,y1,y0,'queste sono le suddivisioni'
        p1=recMolt(x1+x0,y1+y0,lenght)
        p2=recMolt(x1,y1,lent-lent/2)
        p3=recMolt(x0,y0,lent/2)
        print p1,p2,p3,'sono p1,p2,p3 con karatsuba'
        print (x1+x0)*(y1+y0),x1*y1,x0*y0,'sono p1,p2,p3 con python'
        print p2*10**(lent),(p1-p2-p3)*10**(lent/2),p3
        print 'questo e lent',lent
        c= p2*10**(2*(lent/2))+(p1-p2-p3)*10**(lent/2)+p3
        print c,'questo e karatsuba'
        print a*b,'questo e python'
        return p2*10**(2*(lent/2))+(p1-p2-p3)*10**(lent/2)+p3

res=karatsuba(6387,464618)
print res
print 6387*464618

def maxLen(a,b):
    str1=str(a) 
    str2=str(b)
    if len(str1)>len(str2):
        return len(str1)
    else:
        return len(str2)
def trueK(a,b):
    if a<10 or b<10:
        return a*b
    m=maxLen(a,b)
    m2=m/2
    x1=a/10**m2
    x0=a%10**m2
    y1=b/10**m2
    y0=b%10**m2
    p1=trueK(x1+x0,y1+y0)
    p2=trueK(x1,y1)
    p3=trueK(x0,y0)
    return p2*(10**(2*m2))+(p1-p2-p3)*(10**m2)+p3
import random
n=random.randint(0,100000)
m=random.randint(0,100000)
res=trueK(n,m)
print res
print n*m

def fibM(n): 
    if n==0:
        return 0
    else:
        A=[[1,1],[1,0]]
        M=potenzaDiMatrice(A,n-1)
        return M[0][0]
def potenzaDiMatrice(A,k):
    if k==0:
        return [[1,0],[0,1]]
    else:
        M=potenzaDiMatrice(A,k/2)
        M=prodotto(M,M)
        if k%2!=0:
            M=prodotto(M,A)
        return M
def prodotto(M1,M2):
    lista=[]
    for i in range(len(M1)):
        lista.append([])
        for p in range(len(M2)):
            col=colonna(M2,p)
            lista[i].append(prodottoScalare(M1[i], col))
    return lista
def prodottoScalare(riga,colonna):
    res=0  
    for i in range(len(riga)):
        res=res+riga[i]*colonna[i]
    return res
def colonna(M,j):
    lista=[]
    for i in M:
        lista.append(i[j])
    return lista

D=fibM(100)
print D
              
        
            
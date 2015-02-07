from difflib import restore
class number:
    def __init__(self,numb):
        self.str=str(numb)
        self.len=len(self.str)
def somma(a,b):
    add1=number(a)
    add2=number(b)
    final=''
    carry=0
    if add1.len==add2.len:
        for i in range(add2.len-1,-1,-1):
            resBit=str(int(add1.str[i])+int(add2.str[i])+carry)
            if i!=0:
                if len(resBit)>1:
                    final=resBit[1]+final
                    carry=int(resBit[0])
                else:
                    final=resBit+final
                    carry=0  
            else:
                final=resBit+final             
    elif add1.len>add2.len:
        for i in range(add2.len):
            resBit=str(int(add1.str[add1.len-i-1])+int(add2.str[add2.len-i-1])+carry)
            if i!=add2.len-1:
                if len(resBit)>1:
                    final=resBit[1]+final
                    carry=int(resBit[0])
                else:
                    final=resBit+final
                    carry=0  
            else:
                if len(resBit)>1:
                    final=resBit[1]+final
                    j=add1.len-add2.len-1
                    while True:
                        resBit=str(int(add1.str[j])+int(resBit[0]))
                        if j==0:
                            final=resBit+final
                            break
                        else:
                            if len(resBit)>1:
                                final=resBit[1]+final
                                j=j-1
                            else:
                                final=add1.str[:j-1]+resBit+final
                                break
                else:
                    final=add1.str[:add1.len-i-1]+resBit+final
    elif add1.len<add2.len:
        for i in range(add1.len):
            resBit=str(int(add1.str[add1.len-i-1])+int(add2.str[add2.len-i-1])+carry)
            if i!=add1.len-1:
                if len(resBit)>1:
                    final=resBit[1]+final
                    carry=int(resBit[0])
                else:
                    final=resBit+final
                    carry=0  
            else:
                if len(resBit)>1:
                    final=resBit[1]+final
                    j=add2.len-add1.len-1
                    while True:
                        resBit=str(int(add2.str[j])+int(resBit[0]))
                        if j==0:
                            final=resBit+final
                            break
                        else:
                            if len(resBit)>1:
                                final=resBit[1]+final
                                j=j-1
                            else:
                                final=add2.str[:j-1]+resBit+final
                                break
                else:
                    final=add2.str[:add2.len-i-1]+resBit+final
    return int(final)

def somma1(a,b):
    add1=number(a)
    add2=number(b)
    if add1.len<10 and add2.len<10:
        return a+b
    else:
        return int(sommaPartizionata(add1.str,add2.str))
def sommaPartizionata(num1,num2):
    #num1 and num2 are two strings this time
    index1=len(num1)
    index2=len(num2)
    final=''
    carry=0
    while True:
        if len(num1[:index1])<10 or len(num2[:index2])<10:
            if len(num1[:index1])==0 and len(num2[:index2])==0:
                return final
            elif len(num1[:index1])==0:
                final=str(int(num2[:index2])+carry)+final
                return final
            elif len(num2[:index2])==0:
                final=str(int(num1[:index1])+carry)+final  
                return final                           
            elif len(num2[:index2])>=10:
                resulting=str(int(num1[:index1])+int(num2[index2-9:index2])+carry)
                if len(resulting)>=10:
                    final=str(int(num2[:index2-9])+1)+resulting[1:]+final
                    return final
                while len(resulting)<9:
                    resulting='0'+resulting
                return num2[:index2-9]+resulting+final
            elif len(num1[:index1])>=10:
                resulting=str(int(num1[index1-9:index1])+int(num2[:index2])+carry)
                if len(resulting)>=10:
                    final=str(int(num1[:index1-9])+1)+resulting[1:]+final
                    return final
                while len(resulting)<9:
                    resulting='0'+resulting
                return num1[:index1-9]+resulting+final
            else:
                final=str(int(num1[:index1])+int(num2[:index2])+carry)+final   
                return final    
        resulting=str(int(num1[index1-9:index1])+int(num2[index2-9:index2])+carry)   
        if len(resulting)>=10:
            final=resulting[1:]+final
            carry=1
        else:
            while len(resulting)<9:
                resulting='0'+resulting
            final=resulting+final
            carry=0
        index1=index1-9
        index2=index2-9
        
class longInt:
    def __init__(self,maxVal=0,resto=0):
        self.maxVal=maxVal#ounter dei maxValue
        self.resto=resto
    def stampa(self):
        print str(self.maxVal)+str(self.resto)
    
maxValue=1000000000
        
        
def somma3(a,b):
    #ammettiamo che i parametri sono della calsse longInt
    c=longInt()
    c.maxVal=a.maxVal+b.maxVal
    c.resto=a.resto+b.resto
    if c.resto>=1000000000:
        c.maxVal+=1   
        c.resto=c.resto-1000000000
    return c
    

def smartIterative(n):
    start=time()
    a=longInt(0,0)
    b=longInt(0,1)
    for i in range(2,n+1):
        c=somma3(a,b)
        a=b
        b=c
    c.stampa()
    print c.maxVal
    end=time()
    print end-start
    
     
    
        
    
     
from random import randint
from time import time
def prova():
    a=randint(0,10000000000000000000000000000000000000000000000000000000000000000000000)
    b=randint(0,10000000000000000000000000000000000000000000000000000000000000000000000)
    c=randint(0,10)
    print a,b,c
    j=somma(b,a)
    k=somma1(b,a)
    x=somma(c,b)
    y=somma1(c,b)
    print k
    print a+b
    print y
    print c+b
def fib(n):
    start=time()
    a=0
    b=1
    for i in range(2,n+1):
        c=somma(a,b)
        a=b
        b=c
    print c
    end=time()
    print end-start
n=randint(0,10000)
def fib1(n):
    start=time()
    a=0
    b=1
    for i in range(2,n+1):
        c=somma1(a,b)
        a=b
        b=c
    print c
    end=time()
    print end-start
def fib2(n):
    start=time()
    a=0
    b=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    print c
    end=time()
    print end-start
def recfib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return recfib(n-1)+recfib(n-2)
import cProfile
import pstats
if __name__=='__main__':
    smartIterative(100)
    fib2(100)
                    

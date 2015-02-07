def somma3(a,b):
    #ammettiamo che i parametri sono della calsse longInt
    c=long()
    c.maxVal=sommaPartizionata(a.maxVal,b.maxVal)
    c.resto=a.resto+b.resto
    if c.resto>=1000000000:  
        c.resto=c.resto-1000000000
        c.maxVal=sommaPartizionata(c.maxVal,'1')   
    return c
maxValue=1000000000   
def smartIterative(n):
    start=time()
    a=long(0)
    b=long(1)
    for i in range(2,n+1):
        c=somma3(a,b)
        a=b
        b=c
    c.stampa()
    end=time()
    print end-start
class long:
    def __init__(self,resto=0):
        self.maxVal='0'                                #counter dei maxValue
        self.resto=resto
    def stampa(self):
        print self.maxVal+str(self.resto)
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
from time import time
from Progetto_Fibonacci_LongInt.prova2 import fib2
from random import randint
if __name__=='__main__':
    smartIterative(10000)
    fib2(10000) 
    a=randint(0,10000000000000000000000000000)
    b=randint(0,1000000000000000000000000)
    print a+b
    print sommaPartizionata(str(a),str(b))


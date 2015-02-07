from list.LinkedList import Record, ListaCollegata
from list.DoubleLinkedList import DoubleRecord, ListaDoppiamenteCollegata
from Progetto_Fibonacci_LongInt.prova2 import fib2
MaxValue=1000000000
from random import randint
from time import time
from Progetto_Fibonacci_LongInt.prova2 import fib1,number,somma1
import cProfile
import pstats
class longInt:
    
    def __init__(self,number):
        self.number=ListaDoppiamenteCollegata()
        self.number.addAsFirst(number)
    
    def stampaNumero(self):
        if self.number.first==None:
            print ""
            return
        s=""
        current=self.number.first
        while current!=None:
            val=str(current.elem)
            if current!=self.number.first:
                while len(val)<9:
                    val='0'+val
            current=current.next
            s+=val
        print s
class longInt2:
    def __init__(self,number):
        self.number=[number]
        self.lenNumber=1
    def stampaNumero(self):
        s=''
        for i in range(self.lenNumber):
            val=str(self.number[i])
            if i!=0:
                while len(val)<9:
                    val='0'+val
            s+=val 
        print s

def somma(a,b):
    #a and b are two longInt objects
    add1,add2=a.number.last,b.number.last
    res=add1.elem+add2.elem
    if res>=MaxValue:
        carry=1
        res=res%MaxValue
    else:
        carry=0
    c=longInt(res)
    add1,add2=add1.prev,add2.prev
    while (add1!=None and add2!=None):
        res=add1.elem+add2.elem+carry
        if res>=MaxValue:
            carry=1
            res=res%MaxValue
        else:
            carry=0
        c.number.addAsFirst(res)
        add1,add2=add1.prev,add2.prev
    if add1==None and add2==None:
        if carry==1:
            c.number.addAsFirst(carry)
    elif add1==None:
        res=add2.elem+carry
        if res>=MaxValue:
            c.number.addAsFirst(res%MaxValue)
            c.number.addAsFirst(1)
        c.number.addAsFirst(res)        
    else:
        res=add1.elem+carry
        if res>=MaxValue:
            c.number.addAsFirst(res%MaxValue)
            c.number.addAsFirst(1)
        c.number.addAsFirst(res)
    return c

def sommaSpecial(a,b):
    #a and b are two longInt objects
    index1,index2=a.lenNumber-1,b.lenNumber-1
    add1,add2=a.number[index1],b.number[index2]
    res=add1+add2
    index1,index2=index1-1,index2-1
    if res>=MaxValue:
        carry=1
        res=res%MaxValue
    else:
        carry=0
    c=longInt2(res)
    while (index1>=0 and index2>=0):
        res=a.number[index1]+b.number[index2]+carry
        if res>=MaxValue:
            carry=1
            res=res%MaxValue
        else:
            carry=0
        c.number=[res]+c.number
        c.lenNumber+=1
        index1,index2=index1-1,index2-1
    if index1<0 and index2<0:
        if carry==1:
            c.number=[carry]+c.number
            c.lenNumber+=1
    elif index1<0:
        res=b.number[index2]+carry
        if res>=MaxValue:
            c.number=[res%MaxValue]+c.number
            c.number=[1]+c.number
            c.lenNumber+=2
        c.number=[res]+c.number 
        c.lenNumber+=1     
    else:
        res=a.number[index1]+carry
        if res>=MaxValue:
            c.number=[res%MaxValue]+c.number
            c.number=[1]+c.number
            c.lenNumber+=2
        c.number=[res]+c.number
        c.lenNumber+=1
    return c
def conclusion(int1,int2,int3,carry):
    if int1==None and int2==None:
        if carry==0:
            return
        int3.number.addAsFirst(carry)
    elif int1==None:
        res=int2.elem+carry
        if res>=MaxValue:
            int3.number.addAsFirst(res%MaxValue)
            int3.number.addAsFirst(1)
    else:
        res=int1.elem+carry
        if res>=MaxValue:
            int3.number.addAsFirst(res%MaxValue)
            int3.number.addAsFirst(1)
def fibh(n):
    start=time()
    a=longInt(0)
    b=longInt(1)
    for i in range(2,n+1):
        c=somma(a,b)
        a=b
        b=c
    end=time()
    print end-start
    return c
def fibg(n):
    start=time()
    a=longInt2(0)
    b=longInt2(1)
    for i in range(2,n+1):
        c=sommaSpecial(a,b)
        a=b
        b=c
    end=time()
    print end-start
    return c
    
def fib(n):
    fibh(n).stampaNumero()
def fibs(n):
    c=fibg(n)
    c.stampaNumero()
    
if __name__=='__main__':
    n=randint(0,10000)
    print n
    cProfile.run('fib(n)','file')
    p=pstats.Stats('file')
    p.strip_dirs().sort_stats( "time"). print_stats ()
    cProfile.run('fib2(n)','file')
    p=pstats.Stats('file')
    p.strip_dirs().sort_stats( "time"). print_stats ()
    cProfile.run('fib1(n)','file')
    p=pstats.Stats('file')
    p.strip_dirs().sort_stats( "time"). print_stats ()
    cProfile.run('fibs(n)','file')
    p=pstats.Stats('file')
    p.strip_dirs().sort_stats( "time"). print_stats ()
    
    
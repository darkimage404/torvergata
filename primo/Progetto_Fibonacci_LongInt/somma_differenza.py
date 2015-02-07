'''
Created on 01/feb/2015

@author: Francesco

'''
MaxV=1000000000
MaxValue=1000000000
class Long:
    def __init__(self,a=None,sign='+'):
        self.number=a
        if a!=None:
            self.len=len(self.number)
        self.sign=sign
        
def sommaGen(el1,el2):
    if el2.sign=='-':
        return Long(recdiff(el1.number,el2.number,el1.len,el2.len))
    return Long(recsomma((el1.number,el2.number,el1.len,el2.len)))
def somma(a,b):
    if a<1000000000 and b<1000000000:
        return a+b
    add1=str(a)
    add2=str(b)
    leng1=len(add1)
    leng2=len(add2)
    return recsomma(add1,add2,leng1,leng2)
    
    
def recsomma(stra,strb,lenght1,lenght2,carry=0):
    index1=lenght1-9
    index2=lenght2-9
    if index1<=0 and index2<=0:
        if lenght1!=0 and lenght2!=0:
            return str(int(stra[:lenght1])+int(strb[:lenght2])+carry)
        elif lenght1==0:
            return str(int(strb[:lenght2])+carry)
        else:
            return str(int(stra[:lenght1])+carry)
    elif index1<=0:
        if lenght1!=0:
            res=int(stra[:lenght1])+int(strb[index2:lenght2])+carry
            if res>=MaxV:
                return recsomma(strb,'1',index2,1)+(str(res))[1:]
            final=str(res)
            if res<=99999999:
                lres=len(final)
                final='0'*(9-lres)+final
            return strb[:index2]+final
        else:
            res=int(strb[index2:lenght2])+carry
            if res>=MaxV:
                return recsomma(strb,'1',index2,1)+(str(res))[1:]
            final=str(res)
            if res<=99999999:
                lres=len(final)
                final='0'*(9-lres)+final
            return strb[:index2]+final
    elif index2<=0:
        if lenght2!=0:
            res=int(strb[:lenght2])+int(stra[index1:lenght1])+carry
            if res>=MaxV:
                return recsomma(stra,'1',index1,1)+(str(res))[1:]
            final=str(res)
            if res<=99999999:
                lres=len(final)
                final='0'*(9-lres)+final
            return stra[:index1]+final
        else:
            res=int(stra[index1:lenght1])+carry
            if res>=MaxV:
                return recsomma(stra,'1',index1,1)+(str(res))[1:]
            final=str(res)
            if res<=99999999:
                lres=len(final)
                final='0'*(9-lres)+final
            return stra[:index1]+final
    else:
        res=int(stra[index1:lenght1])+int(strb[index2:lenght2])+carry
        if res>=MaxV:
            return recsomma(stra,strb,index1,index2,1)+(str(res))[1:]
        final=str(res)
        if res<=99999999:
            lres=len(final)
            final='0'*(9-lres)+final
        return recsomma(stra,strb,index1,index2)+final
    
def recdiff(stra,strb,lenght1,lenght2,carry=0):
    index1=lenght1-9
    index2=lenght2-9
    if index1<=0 and index2<=0:
        if lenght1!=0 and lenght2!=0:
            return str(int(stra[:lenght1])-int(strb[:lenght2])-carry)
        elif lenght1==0:
            return str(int(strb[:lenght2])-carry)
        else:
            return str(int(stra[:lenght1])-carry)
    elif index2<=0:
        if lenght2!=0:
            res=int(stra[index1:lenght1])-int(strb[:lenght2])-carry
            if res<0:
                return recdiff(stra,'1',index1,1)+(str(res+10000000000))[1:]
            final=str(res)
            if res<=99999999:
                lres=len(final)
                final='0'*(9-lres)+final
            return stra[:index1]+final
        else:
            res=int(stra[index1:lenght1])-carry
            if res<0:
                return recdiff(stra,'1',index1,1)+(str(res+10000000000))[1:]
            final=str(res)
            if res<=99999999:
                lres=len(final)
                final='0'*(9-lres)+final
            return stra[:index1]+final
    else:
        res=int(stra[index1:lenght1])-int(strb[index2:lenght2])-carry
        if res<0:
            return recdiff(stra,strb,index1,index2,1)+(str(res+10000000000))[1:]
        final=str(res)
        if res<=99999999:
            lres=len(final)
            final='0'*(9-lres)+final
    return recdiff(stra,strb,index1,index2)+final
    
    
from random import randint
from time import time
        

def fib1(n):
    start=time()
    a='0'
    b='1'
    for i in range(2,n+1):
        c=recsomma(a,b,len(a),len(b))
        a=b
        b=c
    print c
    end=time()
    print end-start
def fib(n):
    a=0
    b=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    print c
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
n=randint(0,10000)
m=randint(0,1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
a=fib1(n)
b=fib(n)
if a==b:
    print True
c=fibg(n)
c.stampaNumero()
def prova(n,m):
    if n>=m:
        c= recdiff(str(n),str(m),len(str(n)),len(str(m)))
        d= n-m
        print c
        print d
        if c==str(d):
            print True
    else:
        c= recdiff(str(n),str(m),len(str(n)),len(str(m)))
        d= n-m
        print c
        print d
        if c==str(d):
            print True
#prova(n,m)
    
            
            
        
        
        
        
        
    
    
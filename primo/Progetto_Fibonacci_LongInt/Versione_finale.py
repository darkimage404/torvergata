'''
Created on 06/feb/2015

@author: Francesco
'''
def karatsuba(a,b):
    mol1=str(a)
    mol2=str(b)
    len1=len(mol1)
    len2=len(mol2)
    if len1>len2:
        mol2='0'*(len1-len2)+mol2
    elif len2>len1:
        mol1='0'*(len2-len1)+mol1
    return recMolt(mol1,mol2,len1)
    

def recMolt(a,b,lent):
    if lent<4:
        return str(int(a)*int(b))
    else:
        m=lent/2
        x0=a[-m:]
        x1=a[:lent-m]
        y1=b[:lent-m]
        y0=b[-m:]
        x2=recsomma(x1,x0,lent-m,m)
        y2=recsomma(y1,y0,lent-m,m)
        lenx2=len(x2)
        leny2=len(y2)
        if lenx2>leny2:
            y2='0'*(lenx2-leny2)+y2
        elif leny2>lenx2:
            x2='0'*(leny2-lenx2)+x2
        p1=recMolt(x2,y2,lenx2)
        print 'SONO X2 E Y2',x2,y2,int(x1)+int(x0),int(y1)+int(y0)
        print 'QUESTO e P1', p1,int(x2)*int(y2)
        lenp1=len(p1)
        p2=recMolt(x1,y1,lent-m)
        print 'QUESTO e P2',p2,int(x1)*int(y1)
        lenp2=len(p2)
        p3=recMolt(x0,y0,m)
        print 'QUESTO e P3',p3,int(x0)*int(y0)
        lenp3=len(p3)
        c=recsomma( p2+'0'*(2*m),p3,lenp2+2*m,lenp3)
        print 'QUESTO E RECSOMMA1',c,int(p2)*10**(2*m)+int(p3)
        d=recsomma(p2,p3,lenp2,lenp3)
        print 'QUESTO E RECSOMMA2',d,int(p2)+int(p3)
        d=recdiff(p1,d,lenp1,len(d))+'0'*m
        print 'questo e recdiff',d,(int(p1)-int(p2)-int(p3))*(10**m)
        print 'il finale',int(p2)*10**(2*m)+(int(p1)-int(p2)-int(p3))*(10**m)+int(p3)
        return recsomma(c,d,len(c),len(d))
        
        
    

class Long:
    def __init__(self,a=None,sign='+'):
        self.number=a
        if a!=None:
            self.len=len(self.number)
        self.sign=sign
MaxValue=1000000000 
MaxV=1000000000      
def sommaGen(el1,el2):
    if el2.sign=='-':
        return Long(recdiff(el1.number,el2.number,el1.len,el2.len))
    return Long(recsomma((el1.number,el2.number,el1.len,el2.len)))
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
#n=randint(99999,1000000000)
#m=randint(99999,1000000000)
n=36279921
m=797513405
start=time()
res=karatsuba(n,m)
end=time()
print end-start
print res
print n*m,'python'
print n,m
    
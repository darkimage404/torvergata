
class Heap:
    def _init__(self,l):
        self.heap=l
        self.len=len(l)
    def HeapMax(self):
        if self.len==0:
            return None
        return self.heap[0]
    def maxSon(self,nodoId):
        if self.heap[nodoId*2+1]>self.len-1:
            print "hai selezionato un foglia dell'albero"
            return None
        if self.heap[nodoId*2+2]>self.len-1:
            return self.list[nodoId*2+1]    
        if self.heap[nodoId*2+1]>self.heap[nodoId*2+2]:
            return nodoId*2+1
        else:
            return nodoId*2+2
        
    def fixHeap(self,nodoId):
        son=self.maxSon(nodoId)
        while son!=None and self.heap[son]>self.heap[nodoId]:
                self.heap[son], self.heap[nodoId]= self.heap[nodoId],self.heap[son]
                nodoId=son
                son=self.maxSon(nodoId)
    def fixIns(self,nodoId):
        if self.len==1 or self.len==0:
            return
        else:
            father=(nodoId-1)/2
            son=nodoId
            while father>=0 and son<father:
                self.heap[father],self.heap[son]=self.heap[son],self.heap[father]
                son=father
                father=(son-1)/2
            self.fixHeap(father)
             
        
    def insert(self,elem):
        self.heap.append(elem)
        self.fixIns(self.len) #it's not an error:self.len is the value of the last element i inserted
        self.len=self.len+1            
            
    # note:we're working trough side effect
    def heapify(self):
        return self.recHeap(0,self.len-1)
    def recHeap(self,first,last):
        if first>last:
            return
        self.recHeap(first*2+1,last)
        self.recHaep(first*2+2,last)
        self.fixHeap(first)
    def deleteMax(self):
        if self.len==0:
            return None
        maxVal=self.heap[0]
        self.heap[0],self.heap[self.len-1]=self.heap[self.len-1],maxVal
        self.len=self.len-1
        self.fixHaep(0)
        return maxVal
    def representDiff(self):
        self.heapify()
        radix=self.heap[0]
        for i in range(1,self.len):
            self.heap[i]=radix-self.heap[i]
    def increment(self,incr):
        self.representDiff()
        self.heap[0]=self.heap[0]+incr
    def decrement(self,decr):
        self.representDiff()
        self.heap[0]=self.heap[0]+decr
            
        
def heapSort(l):
    #l is a list
    h=Heap(l)
    h.heapify()
    while h.len!=0:
        h.deleteMax()
    return h.heap

def Min(l):
    if len(l)==0:
        return None
    else:
        m=l[0]
        i=1
        while i<len(l):
            if l[i]<m:
                m=l[i]
            i=i+1
        return m
def inf(a,b):
    #a and b are numbers
    if a<b:
        return a
    return b
 
def mergeSort(l): 
    if len(l)==0:
        return
    if len(l)==1:
        return l
    l1=mergeSort(l[:len(l)/2])
    l2=mergeSort(l[len(l)/2:])
    ordl=[]
    while len(l1)!=0 and len(l2)!=0:
        if l1[0]<l2[0]:
            ordl.append(l1[0])
            l1=l1[1:]
        else:
            ordl.append(l2[0])
            l2=l2[1:]  
    if len(l1)==0:
        ordl.extend(l2)
    else:
        ordl.extend(l1)
    return ordl
              
import random        
def quickSort(l): 
    if len(l)==0:
        return 
    return recQsort(l,0,len(l)-1) 
def recQsort(l,start,end):
    if start>end:
        return 
    mid=partition(l,start,end)
    recQsort(l,start,mid-1)
    recQsort(l,mid+1,end)
def partition(l,start,end):
    inf=start
    sup=end
    mid= random.randint(start,end)
    l[start],l[mid]=l[mid],l[start]
    while True:
        inf=inf+1
        while inf<[end] and l[inf]<l[start]:
            inf=inf+1
        while sup>start and l[sup]>l[start]:
            sup=sup-1
        if inf<sup:
            l[inf],l[sup]=l[sup],l[inf]
        else:
            break
    l[start],l[sup]=l[sup],l[start]
    return sup
        
        
def quickSelect(l,k):
    if k>=len(l):
        return None
    recquickSelect(l,k,0,len(l)-1)
def recquickSelect(l,k,start,end):        
    if start==end==k:
        return l[k]
    else:
        piv=partition(l,start,end)
        if k==piv:
            return l[k]
        if k<piv:
            return recquickSelect(l,k,start,piv-1)      
        if k>piv:
            return recquickSelect(l,k,piv+1,end)


    
        
    
              

                
            
        
        
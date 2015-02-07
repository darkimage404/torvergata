from linked_ds.list.LinkedList import ListaCollegata
from linked_ds.queue.Queue import CodaArrayList_deque as queue

class BinomialHeapNode:
    def __init__(self, e, k):
        self.elem = e
        self.key = k
        self.father = None
        self.sons = ListaCollegata()

    def swap(self, otherNode):
        self.elem, otherNode.elem = otherNode.elem, self.elem
        self.key, otherNode.key = otherNode.key, self.key

    def addSon(self, son):
        son.father = self
        self.sons.addAsLast(son)

class BinomialHeap:
    def __init__(self, e, k):
        self.root = BinomialHeapNode(e, k)

    def merge(self, otherHeap):
        thisRoot = self.root
        otherRoot = otherHeap.root
        
        if thisRoot.key <= otherRoot.key:
            otherRoot.father = thisRoot
            thisRoot.addSon(otherRoot)
            return self
        else:
            thisRoot.father = otherRoot
            otherRoot.addSon(thisRoot)
            return otherHeap

    def getHeapSons(self):
        res = ListaCollegata()
        curr = self.root.sons.getFirstRecord()
        while curr != None:
            nHeap = BinomialHeap(None, None)
            nHeap.root = curr.elem
            nHeap.root.father = None
            res.addAsLast(nHeap)
            curr = curr.next
        return res
    
    def stampa(self):
        # bfs
        q = queue()
        q.enqueue((None, self.root))
        while not q.isEmpty():
            father, curr = q.dequeue()
            print father, '-->', curr.key
            if not curr.sons.isEmpty():
                f = curr.sons.getFirstRecord()
                while f != None:
                    q.enqueue((curr.key, f.elem))
                    f = f.next

class PQbinomialHeap:
    maxSize = 32
    def __init__(self):
        # Memorizziamo fino a B31 (e' gia' abbastanza grande!)
        # E' una lista di liste: transitoriamente e' possibile avere fino a 3 heap dello stesso tipo
        self.heap = PQbinomialHeap.maxSize * [None]
        for i in range(len(self.heap)):
            self.heap[i]=[None, None, None]


    # Assume che se heap[i][j]==None, allora anche heap[i][j+1]==None
    def rebuild(self):
        for i in range(len(self.heap)):
            if self.heap[i][1] == None and self.heap[i][2] == None:
                continue
            
            if self.heap[i][1] != None and self.heap[i][2] != None:  # merge the last 2
                merged = self.heap[i][1].merge(self.heap[i][2])
                self.heap[i][1] = None
                self.heap[i][2] = None
            else:  # merge the (only) first two
                merged = self.heap[i][0].merge(self.heap[i][1])
                self.heap[i][0] = None
                self.heap[i][1] = None
    
            if self.heap[i + 1][0] == None:
                self.heap[i + 1][0] = merged
            elif self.heap[i + 1][1] == None:
                self.heap[i + 1][1] = merged
            else:
                self.heap[i + 1][2] = merged

    def isEmpty(self):
        for i in range(len(self.heap)):
            if self.heap[i][0] != None:
                return False
        return True

    # Si aggiunge un B0, e poi si ristruttura
    def insert(self, e, k):
        nHeap = BinomialHeap(e, k)
        root = nHeap.root
        if self.heap[0][0] == None:
            self.heap[0][0] = nHeap
        else:
            self.heap[0][1] = nHeap
            self.rebuild()
        return root

    # restituisce l'indice dell'heap binomiale la cui radice e' il nodo di chiave minima
    def findMinIndex(self):
        if self.isEmpty():
            return -1
        # find first non empty position
        for besti in range(PQbinomialHeap.maxSize):
            if self.heap[besti][0] != None:
                break
        # find best index
        for i in range(besti + 1, PQbinomialHeap.maxSize):
            if self.heap[i][0] != None and self.heap[i][0].root.key < self.heap[besti][0].root.key:
                besti = i
        return besti
    
    def findMin(self):
        if self.isEmpty():
            return None
        return self.heap[self.findMinIndex()][0].root.elem

    def deleteMin(self):
        if self.isEmpty():
            return
        index = self.findMinIndex()
        nuovi = self.heap[index][0].getHeapSons()  # take the sons of the B_index tree
        # self.heap[index][0].stampa()
        self.heap[index][0] = None  # cut the unique B_index tree 
        count = 0
        curr = nuovi.getFirstRecord()  # assume these are B_0, ..., B_index-1 trees in order
        while curr != None:
            # print count,curr
            if self.heap[count][0] == None:
                self.heap[count][0] = curr.elem
            else:
                self.heap[count][1] = curr.elem
            count += 1
            curr = curr.next
        
        self.rebuild()
    
    def stampa(self):
        for i in range(len(self.heap)):
            if self.heap[i][0] is not None:
                print "B_" + str(i)
                self.heap[i][0].stampa()
            
            
if __name__ == "__main__":
    pq = PQbinomialHeap()
    if pq.isEmpty():
        print "Empty queue"
    
    e = 4.0
    k = 2.0
    print "insert({},{})".format(e, k)
    pq.insert(e, k)
    pq.stampa()
    print "findMin():", pq.findMin()
    
    e = 2.0
    k = 1.0
    print "insert({},{})".format(e, k)
    pq.insert(e, k)
    pq.stampa()
    print "findMin():", pq.findMin()
    
    e = 8.0
    k = 4.0
    print "insert({},{})".format(e, k)
    pq.insert(e, k)
    pq.stampa()
    print "findMin():", pq.findMin()
    
    e = 10.0
    k = 5.0
    print "insert({},{})".format(e, k)
    pq.insert(e, k)
    pq.stampa()
    print "findMin():", pq.findMin()
    
    e = 6.0
    k = 3.0
    print "insert({},{})".format(e, k)
    pq.insert(e, k)
    pq.stampa()
    print "findMin():", pq.findMin()
    
    print "deleteMin()"
    pq.deleteMin()
    pq.stampa()
    print "findMin():", pq.findMin()
    
    e = 12.0
    k = 6.0
    print "insert({},{})".format(e, k)
    pq.insert(e, k)
    e = 14.0
    k = 7.0
    print "insert({},{})".format(e, k)
    pq.insert(e, k)
    e = 16.0
    k = 8.0
    print "insert({},{})".format(e, k)
    pq.insert(e, k)
       
    print "deleteMin()"
    pq.deleteMin()
    pq.stampa()
                
    e = 4.0
    k = 2.0
    print "insert({},{})".format(e, k)
    pq.insert(e, k)
    e = 2.0
    k = 1.0
    print "insert({},{})".format(e, k)
    pq.insert(e, k)
    pq.stampa()

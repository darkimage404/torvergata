from priorityQueue.PQ_Dheap import PQ_DHeap
from priorityQueue.PQbinaryHeap import PQbinaryHeap
from priorityQueue.PQbinomialHeap import PQbinomialHeap
from time import time
from random import randrange
from random import random

def testPQ1(pqType, collection, d=None):
    # collection=[ (elem,key), ...]
    if pqType == 'PQbinary':
        pq = PQbinaryHeap()
        print "Testing", pqType
    elif pqType == 'PQbinomial':
        pq = PQbinomialHeap()
        print "Testing", pqType
    elif pqType == 'PQ_Dheap' and d is not None:
        pq = PQ_DHeap(d)
        print "Testing", pqType, "with d=", d
    else:
        return
    
    size = len(collection)
    start = time()    
    for e in collection:
        pq.insert(e[0], e[1])
    elapsed = time() - start
    print "Insert running time (average over {} calls): {}, total: {}".format(size, float(elapsed) / size, float(elapsed))
    start = time()    
    while not pq.isEmpty():
        pq.deleteMin()
    elapsed = time() - start
    print "DeleteMin running time (average over {} calls): {}, total: {}".format(size, float(elapsed) / size, float(elapsed))

def testPQ2(pqType, collection, p, d=None):
    # collection=[ (elem,key), ...]
    # p is probability of deleting an element => p in [0,1]
    if pqType == 'PQbinary':
        pq = PQbinaryHeap()
        print "Testing", pqType
    elif pqType == 'PQbinomial':
        pq = PQbinomialHeap()
        print "Testing", pqType
    elif pqType == 'PQ_Dheap' and d is not None:
        pq = PQ_DHeap(d)
        print "Testing", pqType, "with d=", d
    else:
        return
    
    size = len(collection)
    start = time()
    nins = 0
    ndel = 0    
    for i in range(size):
        if i < size / 2:
            e = collection[i]
            pq.insert(e[0], e[1])
            nins += 1
        else:
            r = random()
            if r < p:
                pq.deleteMin()
                ndel += 1
            else:
                e = collection[i]
                pq.insert(e[0], e[1])
                nins += 1
    elapsed = time() - start
    print "Overall running time of mixed operations ({} inserts and {} deletes): {}".format(nins, ndel, float(elapsed))

if __name__ == "__main__":
    collSize = 200000
    rand = False

    collection = []
    for i in range(collSize):
        if rand:
            k = randrange(0, collSize)
        else:
            k = i
        collection.append([2 * k, k])
    
    t1 = False
    if t1:
        testPQ1('PQbinary', collection)
        testPQ1('PQbinomial', collection)
        testPQ1('PQ_Dheap', collection, 2)
        testPQ1('PQ_Dheap', collection, 4)
        testPQ1('PQ_Dheap', collection, 8)
        testPQ1('PQ_Dheap', collection, 16)
        testPQ1('PQ_Dheap', collection, 32)
        testPQ1('PQ_Dheap', collection, 64)
    else:
        for p in [0.4, 0.6, 0.8, 1.0]:
            print "Test for p=", p
            testPQ2('PQbinary', collection, p)
            testPQ2('PQbinomial', collection, p)
            testPQ2('PQ_Dheap', collection, p, 2)
            testPQ2('PQ_Dheap', collection, p, 4)
            testPQ2('PQ_Dheap', collection, p, 8)
            testPQ2('PQ_Dheap', collection, p, 16)
            testPQ2('PQ_Dheap', collection, p, 32)
            testPQ2('PQ_Dheap', collection, p, 64)
            print 30*"*"

from UnionFind_QuickFind import UnionFindQuickFind
from UnionFind_BalancedQuickFind import UnionFindBalancedQuickFind
from UnionFind_QuickUnion import UnionFindQuickUnion
from UnionFind_BalancedQuickUnion import UnionFindBalancedQuickUnion
from UnionFind_QuickUnion_PathCompression import UnionFindQuickUnionPathCompression
from random import random
from random import randint
from time import time
    
def testUnionFind(amount,nCalls,pFind,simple):
    sequence=[]
    for _ in range(nCalls):
        choice=random()
        if choice<=pFind:
            n=randint(0,amount-1)
            sequence.append(('f',n))
        else:
            n1=randint(0,amount-1)
            n2=n1
            while n2==n1:
                n2=randint(0,amount-1)
            sequence.append(('u',n1,n2))
    
    if simple:
        print "UnionFindQuickFind"
        nodes=[]
        uf=UnionFindQuickFind()
        for i in range(amount):
            nodes.append(uf.makeset(i).sons.getFirstRecord().elem)
        start=time()
        for s in sequence:
            if s[0]=='f':
                uf.find(nodes[s[1]])
            else:
                uf.union(uf.findRoot(nodes[s[1]]), uf.findRoot(nodes[s[2]]))
        elapsed=time()-start
        print "Sequence of {} calls over {} elements with Find probability {} took {} seconds.\n".format(nCalls,amount,pFind,elapsed)
    
    print "UnionFindQuickFind bilanciato"
    nodes=[]
    uf=UnionFindBalancedQuickFind()
    for i in range(amount):
        nodes.append(uf.makeset(i).sons.getFirstRecord().elem)
    start=time()
    for s in sequence:
        if s[0]=='f':
            uf.find(nodes[s[1]])
        else:
            uf.union(uf.findRoot(nodes[s[1]]), uf.findRoot(nodes[s[2]]))
    elapsed=time()-start
    print "Sequence of {} calls over {} elements with Find probability {} took {} seconds.\n".format(nCalls,amount,pFind,elapsed)
    
    if simple:
        print "UnionFindQuickUnion"
        nodes=[]
        uf=UnionFindQuickUnion()
        for i in range(amount):
            nodes.append(uf.makeset(i)) #watch it!
        start=time()
        for s in sequence:
            if s[0]=='f':
                uf.find(nodes[s[1]])
            else:
                uf.union(uf.findRoot(nodes[s[1]]), uf.findRoot(nodes[s[2]]))
        elapsed=time()-start
        print "Sequence of {} calls over {} elements with Find probability {} took {} seconds.\n".format(nCalls,amount,pFind,elapsed)
    
    print "UnionFindQuickUnion bilanciato"
    nodes=[]
    uf=UnionFindBalancedQuickUnion()
    for i in range(amount):
        nodes.append(uf.makeset(i)) #watch it!
    start=time()
    for s in sequence:
        if s[0]=='f':
            uf.find(nodes[s[1]])
        else:
            uf.union(uf.findRoot(nodes[s[1]]), uf.findRoot(nodes[s[2]]))
    elapsed=time()-start
    print "Sequence of {} calls over {} elements with Find probability {} took {} seconds.\n".format(nCalls,amount,pFind,elapsed)
    
    print "UnionFindQuickUnion pathCompression"
    nodes=[]
    uf=UnionFindQuickUnionPathCompression()
    for i in range(amount):
        nodes.append(uf.makeset(i)) #watch it!
    start=time()
    for s in sequence:
        if s[0]=='f':
            uf.find(nodes[s[1]])
        else:
            uf.union(uf.findRoot(nodes[s[1]]), uf.findRoot(nodes[s[2]]))
    elapsed=time()-start
    print "Sequence of {} calls over {} elements with Find probability {} took {} seconds.\n".format(nCalls,amount,pFind,elapsed)
    
if __name__ == '__main__':
    testUnionFind(10000,10000,0.75,True)
    print 10*' '+30*'*'+'\n'
    testUnionFind(10000,10000,0.5,True)
    print 10*' '+30*'*'+'\n'
    testUnionFind(10000,10000,0.25,True)
    print 10*' '+30*'*'+'\n'
    print 10*' '+30*'*'+'\n'
    testUnionFind(100000,100000,0.75,False)
    print 10*' '+30*'*'+'\n'
    testUnionFind(100000,100000,0.5,False)
    print 10*' '+30*'*'+'\n'
    testUnionFind(100000,100000,0.25,False)
    
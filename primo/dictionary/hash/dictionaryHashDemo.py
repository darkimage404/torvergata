from collisionsListHash import DictCollisionListHash
from openIndexingHash import DictOpenIndexingHash
from time import time
from dictionary.dictTrees.dictTreeDemo import testBinary
import hashFunctions

def testHash(steps, collList, hashFunction):
    diz = None
    
    if collList:
        diz = DictCollisionListHash(steps / 5, hashFunction)
    else:
        diz = DictOpenIndexingHash(steps, hashFunction)
    
    print "\nTest di {} (tempo medio per ogni operazione, calcolato su {} chiamate):\n".format(("DictionaryCollisionList" if collList else "DictionaryOpenIndexing"), steps)
    
    start = time()
    for i in range(steps):
        diz.insert(2 * i, i)
    elapsed = time() - start
    print "Tempo medio insert:", elapsed / steps
    
    start = time()
    for i in range(steps):
        diz.search(2 * i)
    elapsed = time() - start
    print "Tempo medio search a buon fine:", elapsed / steps
    
    start = time()
    for i in range(steps):
        diz.search(2 * i + 1)
    elapsed = time() - start
    print "Tempo medio search di elementi non presenti:", elapsed / steps
    
    start = time()
    for i in range(steps):
        diz.delete(2 * i)
    elapsed = time() - start
    print "Tempo medio delete:", elapsed / steps

if __name__=="__main__":
    steps=2000
    testBinary(steps,False)
    testBinary(steps,True)
    
    f1d=hashFunctions.HashFunction_module()
    f1r=hashFunctions.HashFunction_Adv()
    f2=hashFunctions.doubleHash()
    f2linear=hashFunctions.doubleHash_linearScan()
    f2quad=hashFunctions.doubleHash_quadraticScan()
    print "double hash"
    testHash(steps,False,f2)
    print "double hash linear"
    testHash(steps,False,f2linear)
    print "double hash quadratic"
    testHash(steps,False,f2quad)
    print "hash divisione"
    testHash(steps,True,f1d)
    print "hash ripiegamento"
    testHash(steps,True,f1r)

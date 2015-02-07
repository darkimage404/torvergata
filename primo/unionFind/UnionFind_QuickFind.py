from linked_ds.list.LinkedList import ListaCollegata

class NodoUnionFind:
    def __init__(self, e):
        self.elem = e
        self.father = None
        self.sons = ListaCollegata()

class UnionFindQuickFind:
    #OSS: NON memorizziamo gli insiemi nella classe.
    # Serve una struttura ausiliaria esterna.
    
    def makeset(self, e):
        # Costruiamo alberi di altezza 1: le foglie sono gli elementi e la radice e'
        # un nodo contenente copia del rappresentante del set
        root = NodoUnionFind(e)
        son = NodoUnionFind(e)
        root.sons.addAsLast(son)
        son.father = root
        return root
    
    def find(self, node):
        return node.father.elem

    def findRoot(self, node):
        return node.father
    
    def union(self, root1, root2):
        if root2==root1:
            return root1
        # aggiorno il padre dei figli di radice2 a radice1
        curr2 = root2.sons.getFirstRecord()
        while curr2 != None:
            curr2.elem.father = root1
            curr2 = curr2.next
        
        #appendo la lista di figli di r2 alla lista di figli di r1
        #OSS: NON serve un ciclo
        last1 = root1.sons.getLastRecord()
        first2 = root2.sons.getFirstRecord()
        last2 = root2.sons.getLastRecord()
        last1.next = first2
        root1.sons.last = last2
        
        return root1

if __name__ == "__main__":
    uf = UnionFindQuickFind()
    
    nodes = []
    for i in range(10):
        print "makeset(" + str(i) + ")"
        root = uf.makeset(i)
        nodes.append(root.sons.getFirstRecord().elem)
    
    for i in range(10):
        print "find(" + str(i) + ")= " + str(uf.find(nodes[i]))
    
    print "union(radice(0),radice(2))"
    uf.union(uf.findRoot(nodes[0]), uf.findRoot(nodes[2]))
    print("union(radice(8),radice(4))")
    uf.union(uf.findRoot(nodes[8]), uf.findRoot(nodes[4]))
    
    for i in range(10):
        print "find(" + str(i) + ")= " + str(uf.find(nodes[i]))
        
    print "union(radice(0),radice(8))"
    uf.union(uf.findRoot(nodes[0]), uf.findRoot(nodes[8]))
    for i in range(10):
        print "find(" + str(i) + ")= " + str(uf.find(nodes[i]))
    
    print "union(radice(5),radice(8))"
    uf.union(uf.findRoot(nodes[5]), uf.findRoot(nodes[8]))
    for i in range(10):
        print "find(" + str(i) + ")= " + str(uf.find(nodes[i]))

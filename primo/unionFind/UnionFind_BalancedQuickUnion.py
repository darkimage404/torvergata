from unionFind.UnionFind_BalancedQuickFind import NodoUnionFindBilanciato
from unionFind.UnionFind_QuickUnion import UnionFindQuickUnion

class UnionFindBalancedQuickUnion(UnionFindQuickUnion):
    """"Ora l'albero piu' piccolo viene appeso a quello piu' grande"""

    def makeset(self, e):
        """Creiamo un albero con un solo nodo"""
        return NodoUnionFindBilanciato(e)

    def union(self, root1, root2):
        """Appendiamo la radice di un albero alla radice dell'altro"""
        if root1==root2:
            return root1
        
        r1 = root1
        r2 = root2
        if r1.size >= r2.size:
            r2.father = r1
            r1.size += r2.size
            return r1
        else:
            r1.father = r2
            r2.size += r1.size
            return r2


if __name__ == "__main__":
    uf = UnionFindBalancedQuickUnion()
        
    nodes = []
    for i in range(10):
        print "makeset(" + str(i) + ")"
        nodes.append(uf.makeset(i))
    
    for i in range(10):
        print "find({})= {}\t father({})= {}".format(i, uf.find(nodes[i]), i, nodes[i].father.elem if nodes[i].father != None else "None")
    
    print "union(radice(0),radice(2))"
    uf.union(uf.findRoot(nodes[0]), uf.findRoot(nodes[2]))
    print("union(radice(8),radice(4))")
    uf.union(uf.findRoot(nodes[8]), uf.findRoot(nodes[4]))
    
    for i in range(10):
        print "find({})= {}\t father({})= {}".format(i, uf.find(nodes[i]), i, nodes[i].father.elem if nodes[i].father != None else "None")
        
    print "union(radice(0),radice(8))"
    uf.union(uf.findRoot(nodes[0]), uf.findRoot(nodes[8]))
    for i in range(10):
        print "find({})= {}\t father({})= {}".format(i, uf.find(nodes[i]), i, nodes[i].father.elem if nodes[i].father != None else "None")
    
    print "union(radice(5),radice(8))"
    uf.union(uf.findRoot(nodes[5]), uf.findRoot(nodes[8]))
    for i in range(10):
        print "find({})= {}\t father({})= {}".format(i, uf.find(nodes[i]), i, nodes[i].father.elem if nodes[i].father != None else "None")

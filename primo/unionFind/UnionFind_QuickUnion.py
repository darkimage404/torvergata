from unionFind.UnionFind_QuickFind import NodoUnionFind

class UnionFindQuickUnion:
    """ La radice di ciascun albero e' il rappresentante del set corrispondente
        Non utilizziamo la lista di figli perche' non aiuta """
             
    def makeset(self, e):
        """"Creiamo un albero con un solo nodo"""    
        return NodoUnionFind(e)

    def findRoot(self, node):
        #risalgo l'albero
        curr = node
        while curr.father != None:
            curr = curr.father
        return curr

    def find(self, node):
        root = self.findRoot(node)
        return root.elem

    def union(self, root1, root2):
        """" Appendiamo la radice di un albero alla radice dell'altro """
        if root1==root2:
            return root1
        
        root2.father = root1
        return root1

if __name__ == "__main__":
    uf = UnionFindQuickUnion()
        
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

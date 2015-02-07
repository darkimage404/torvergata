from unionFind.UnionFind_QuickFind import NodoUnionFind, UnionFindQuickFind

class NodoUnionFindBilanciato(NodoUnionFind):
    def __init__(self, e):
        NodoUnionFind.__init__(self, e)
        self.size = 1 #NEW!

#Come UnionFindQuickUnion, ma con union bilanciata per size
class UnionFindBalancedQuickFind(UnionFindQuickFind):

    def makeset(self, e):
        root = NodoUnionFindBilanciato(e)
        son = NodoUnionFindBilanciato(e)
        root.sons.addAsLast(son)
        son.father = root
        return root
    
    def union(self, root1, root2):
        """ora la radice con meno figli cede i propri figli all'altra radice"""
        if root1==root2:
            return root1
        
        if root1.size >= root2.size:
            curr2 = root2.sons.getFirstRecord()
            while curr2 != None: #this will be faster...
                curr2.elem.father = root1
                curr2 = curr2.next
            last1 = root1.sons.getLastRecord()
            first2 = root2.sons.getFirstRecord()
            last2 = root2.sons.getLastRecord()
            last1.next = first2
            root1.sons.last = last2
            root1.size += root2.size #watch it!
            
            return root1
        else:
            curr1 = root1.sons.getFirstRecord()
            while curr1 != None:
                curr1.elem.father = root2
                curr1 = curr1.next
            last2 = root2.sons.getLastRecord()
            first1 = root1.sons.getFirstRecord();
            last1 = root1.sons.getLastRecord();
            last2.next = first1
            root2.sons.last = last1
            root2.size += root1.size #watch it!
            
            return root2

if __name__ == "__main__":
    uf = UnionFindBalancedQuickFind()
    
    nodes = []
    for i in range(10):
        print "makeset(" + str(i) + ")"
        root = uf.makeset(i)
        nodes.append(root.sons.getFirstRecord().elem)
    
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

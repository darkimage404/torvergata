from unionFind.UnionFind_BalancedQuickUnion import UnionFindBalancedQuickUnion

class UnionFindQuickUnionPathCompression(UnionFindBalancedQuickUnion):    
    """ 
    Durante le find() utilizziamo l'euristica di path compression
    Si eseguono m find ed n makeset/union in tempo O(n+m*a(m+n,n)) 
    dove a e' l'inversa della funzione di Ackermann A:
    A(m,n)=n+1 se m=0;
    A(m,n)=A(m-1,1) se m>0, n=0;
    A(m,n)=A(m-1,A(m,n-1)) se m>0, n>0;
    a(m,n)=min{i>=1: A(i,floor(m/n))>= log_2 n
    """

    def findRoot(self, node):
        if node.father is None:
            return node
        node.father=self.findRoot(node.father)
        return node.father

if __name__ == "__main__":
    uf = UnionFindQuickUnionPathCompression()
        
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

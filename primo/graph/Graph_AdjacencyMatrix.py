from graph.elements import Node

class GraphAdjacencyMatrix:
    empty = object() #a marker
    
    def __init__(self):
        self.nodes = []
        self.adj = []
        self.nextId = 0
    
    def isAdj(self, tail, head):
        if tail < 0 or tail >= len(self.adj) or head < 0 or head >= len(self.adj):
            return False
        
        if self.adj[tail][head] != GraphAdjacencyMatrix.empty:
            return True
        else:
            return False
    
    def insertNode(self, e,w=None):
        newnode = Node(self.nextId, e,w)
        self.nextId += 1
        self.nodes.append(newnode)
        #Adjust the matrix dimension
        self.adj.append(len(self.adj) * [GraphAdjacencyMatrix.empty])
        for l in self.adj:
            l.append(GraphAdjacencyMatrix.empty)
        return newnode
    
    def insertArc(self, tail, head, weight=None):
        if tail < 0 or tail >= len(self.adj) or head < 0 or head >= len(self.adj):
            return
        self.adj[tail][head] = weight
        
    def deleteArc(self, tail, head):
        if tail < 0 or tail >= len(self.adj) or head < 0 or head >= len(self.adj):
            return
        self.adj[tail][head] = GraphAdjacencyMatrix.empty

    def deleteNode(self, index):
        #Here you have to pay attention in adjusting not only the matrix
        #but even the id of the nodes...
        if index < 0 or index >= len(self.adj):
            return
        
        del self.nodes[index]
        for i in range(index, len(self.nodes)):
            self.nodes[i].index = i
        self.nextId=len(self.nodes)
        
        del self.adj[index]
        for l in self.adj:
            del l[index]

    def simpleSearch(self, root):
        if root < 0 or root >= len(self.adj):
            return
        
        # inizializziamo lo stato dei nodi
        state = len(self.nodes) * [0] #0 means waiting
        
        state[root] = 1 #means open
        
        l = []
        s = set()
        s.add(root)
        
        while len(s)>0:
            #arbitrary pop
            currind = s.pop()
            state[currind] = -1 #means closed
            l.append(self.nodes[currind])
            
            currAdj = self.adj[currind]
            for i in range(len(currAdj)):
                if currAdj[i] != GraphAdjacencyMatrix.empty:
                    # Inseriamo un vicino solo se e' un nodo il cui stato e' waiting
                    if state[i] == 0:
                        state[i] = 1
                        s.add(i)
        return l


    def stampa(self):
        s = " "
        for n in self.nodes:
            s+=str(n.index)+"   "
        s+="\n"
        for a in self.adj:
            for c in a:
                if c == GraphAdjacencyMatrix.empty:
                    s += " -- "
                else:
                    s += str(c) + " "
            s += "\n"
        print s

if __name__ == "__main__":
        G = GraphAdjacencyMatrix();
                
        nodo0 = G.insertNode(0)
        print "nodo0=insertNodo(0)"
        nodo1 = G.insertNode(2)
        print "nodo1=insertNodo(2)"
        nodo2 = G.insertNode(4)
        print "nodo2=insertNodo(4)"
        nodo3 = G.insertNode(6)
        print "nodo3=insertNodo(6)"
        nodo4 = G.insertNode(8)
        print "nodo4=insertNodo(8)"
        nodo5 = G.insertNode(10)
        print "nodo5=insertNodo(10)"
        
        G.insertArc(nodo0.index, nodo2.index, 2.3)
        print "insertArco(nodo0,nodo2,2.3)"
        G.insertArc(nodo3.index, nodo4.index, 1.4)
        print "insertArco(nodo3,nodo4,1.4)"
        G.insertArc(nodo0.index, nodo1.index, 8.1)
        print "insertArco(nodo0,nodo1,8.1)"
        G.insertArc(nodo4.index, nodo3.index, 6.4)
        print "insertArco(nodo4,nodo3,6.4)"
        G.insertArc(nodo5.index, nodo1.index, 6.2)
        print "insertArco(nodo5,nodo1,6.2)"
        G.insertArc(nodo5.index, nodo4.index, 4.1)
        print "insertArco(nodo5,nodo4,4.1)"
        G.insertArc(nodo2.index, nodo3.index, 2.2)
        print "insertArco(nodo2,nodo3,2.2)"
        
        G.stampa()

        print "adiacente(nodo0,nodo2)=" + str(G.isAdj(nodo0.index, nodo2.index))
        print "adiacente(nodo5,nodo2)=" + str(G.isAdj(nodo5.index, nodo2.index))


        print "simpleSearch da nodo0"        
        lista = G.simpleSearch(nodo0.index)
        s = ""
        for n in lista:
            s += str(n.index) + " "
        print s
        
        G.deleteNode(nodo2.index)
        print "deleteNodo(nodo2)"
        G.stampa()
        
        G.deleteArc(nodo4.index, nodo3.index)
        print "deleteArco(nodo4,nodo3)"
        G.stampa();
        
        
        G.deleteNode(nodo3.index)
        print "deleteNodo(nodo3)"
        G.deleteNode(nodo0.index)
        print "deleteNodo(nodo0)"
        G.deleteNode(nodo1.index)
        print "deleteNodo(nodo1)"
        G.stampa()
        

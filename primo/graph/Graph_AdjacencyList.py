from linked_ds.list.DoubleLinkedList import ListaDoppiamenteCollegata as Lista
from graph.elements import Node

class DFSinfo:
    def __init__(self):
        self.t=0
        self.pre=dict()
        self.post=dict()
    
    def stampa(self):
        print "Preorder numbering"
        for i,p in self.pre.iteritems():
            print i,":",p
        print "Postorder numbering"
        for i,p in self.post.iteritems():
            print i,":",p
        

class GraphAdjacencyList:
    def __init__(self):
        self.nodes = None
        self.adj = None
        self.nextId = 0
        
    def isAdj(self, tail, head):
        if not head in self.nodes or not tail in self.nodes:
            return False
        
        curr = self.adj[tail].getFirstRecord()
        while curr != None:
            a = curr.elem
            if a == head:
                return True
            curr = curr.next
        
        return False
    
    def insertNode(self, e, w=None):
        newnode = Node(self.nextId, e, w)
        self.nextId += 1
        if self.nodes == None:
            self.nodes = {newnode.index : newnode}
            self.adj = {newnode.index : Lista()}
        else:
            self.nodes[newnode.index] = newnode
            self.adj[newnode.index] = Lista()
        
        return newnode

    def deleteNode(self, index):
        try:
            del self.nodes[index]
            del self.adj[index]
        except KeyError:
            pass
        
        # Controlla TUTTE le liste di adiacenza e cancella gli archi che puntano al nodo eliminato.
        # E' in generale molto lento.
        # Si puo' fare di meglio, ma dipende dall'applicazione specifica.
        for adj in self.adj.itervalues():
            curr = adj.getFirstRecord()
            while curr != None:
                if curr.elem == index:
                    adj.deleteRecord(curr)
                curr = curr.next
    
    def insertArc(self, tail, head):
        if head in self.nodes and tail in self.nodes:
            self.adj[tail].addAsLast(head)
    
    def deleteArc(self, tail, head):
        if head in self.nodes and tail in self.nodes:
            curr = self.adj[tail].getFirstRecord()
            while curr != None:
                if curr.elem == head:
                    self.adj[tail].deleteRecord(curr)
                curr=curr.next
    
    def simpleSearch(self, root):
        if root not in self.nodes:
            return
        
        # inizializziamo lo stato dei nodi
        state = dict()
        
        state[root] = 1  # means open
        #if a node index is not in the dictionary, as a key, it means its state is 'waiting'.
        #If nodes have consecutive ids starting from 0 and no node has been delete, you can use an array
        # of n elements, where n is the number of nodes, initializing its cells to 0, meaning 'waiting'.
        
        nodesVisited = [] #nodes visited, in order
        s = set()
        s.add(root)
        
        while len(s) > 0:
            # arbitrary pop
            currind = s.pop()
            
            state[currind] = -1  # means closed
            nodesVisited.append(self.nodes[currind])
            curr = self.adj[currind].getFirstRecord()
            
            while curr != None:
                a = curr.elem
                # Inseriamo un vicino solo se e' un nodo il cui stato e' waiting
                if a not in state:
                    state[a] = 1 #open
                    s.add(a)
                curr = curr.next
        
        return nodesVisited
    
    def dfs(self):
        dfsInfo=DFSinfo()
        
        for v in G.nodes.iterkeys():
            if v not in dfsInfo.pre:
                self.DFSrec(v,dfsInfo)
        return dfsInfo
    
    def DFSrec(self,v,dfsInfo):
        dfsInfo.t+=1
        dfsInfo.pre[v]=dfsInfo.t
        
        curr = self.adj[v].getFirstRecord()
        while curr != None:
            if curr.elem not in dfsInfo.pre:
                self.DFSrec(curr.elem,dfsInfo)
            curr = curr.next
        
        dfsInfo.t+=1
        dfsInfo.post[v]=dfsInfo.t
    
    
    def stampa(self):
        for p in self.adj.iteritems():
            print str(p[0]) + ":"
            l = p[1]
            if l.first == None:
                print "[]"
            else:
                s = "["
                current = l.first
                while current != None:
                    if len(s) > 1:
                        s += ", "
                    s += "(" + str(current.elem)+ ")"
                    current = current.next
                s += "]"
                print s

if __name__ == "__main__":
        G = GraphAdjacencyList();
                
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
        
        G.insertArc(nodo0.index, nodo2.index)
        print "insertArco(nodo0,nodo2)"
        G.insertArc(nodo3.index, nodo4.index)
        print "insertArco(nodo3,nodo4)"
        G.insertArc(nodo0.index, nodo1.index)
        print "insertArco(nodo0,nodo1)"
        G.insertArc(nodo4.index, nodo3.index)
        print "insertArco(nodo4,nodo3)"
        G.insertArc(nodo5.index, nodo1.index)
        print "insertArco(nodo5,nodo1)"
        G.insertArc(nodo5.index, nodo4.index)
        print "insertArco(nodo5,nodo4)"
        G.insertArc(nodo2.index, nodo3.index)
        print "insertArco(nodo2,nodo3)"
        
        G.stampa()

        print "adiacente(nodo0,nodo2)=" + str(G.isAdj(nodo0.index, nodo2.index))
        print "adiacente(nodo5,nodo2)=" + str(G.isAdj(nodo5.index, nodo2.index))

        print "simpleSearch da nodo0"        
        lista = G.simpleSearch(nodo0.index)
        s = ""
        for n in lista:
            s += str(n.index) + " "
        print s
        
        print "\nDFS globale"
        dfsInfo=G.dfs()
        dfsInfo.stampa()
        print
        
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
        
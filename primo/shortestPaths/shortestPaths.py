from priorityQueue.PQbinaryHeap import PQbinaryHeap as PriorityQueue
from graph.Graph_AdjacencyList import GraphAdjacencyList as Graph
from __init__ import printSwitch
Dump = printSwitch.dumpOperations
Infinite = float("inf")

class ShortestPaths:
    
    @staticmethod
    def BellmanFordMoore(g, root):
        """O(nm). Restituiamo solo l'array delle distanze dalla radice."""
        n = len(g.nodes)
        if root < 0 or root >= n:
            return
        
        dist = n * [Infinite]
        dist[root] = 0.0
        
        if Dump:
            print "dist:", dist
        
        for k in range(n): #@UnusedVariable
            changed = False
            
            if Dump:
                print "iteration", k
                
            for i in range(n):
                curr = g.adj[i].getFirstRecord()
                while curr != None:
                    e = (i,curr.elem[0],curr.elem[1])
                    #rilassamento
                    if dist[e[0]] != Infinite and dist[e[0]] + e[2] < dist[e[1]]:
                        if Dump:
                            print "Relaxing dist[{}] for edge ({},{}). New distance:{}".format(e.head, e.tail, e.head, dist[e.tail] + e.weight)
                            
                        dist[e[1]] = dist[e[0]] + e[2]
                        changed = True
                    curr = curr.next
            if not changed: #Optimization
                if Dump:
                    print "No updates occurred. Done"
                        
                break
        else:
            if Dump:
                print "No more iterations needed."
        return dist
    
    @staticmethod
    def Dijkstra(g, root):
        """O(m log(n)) con heap binario. Avrebbe impiegato O(m+log(n)) con heap di Fibonacci."""
        
        n = len(g.nodes)
        if root < 0 or root >= n:
            return
        
        pq = PriorityQueue()
        nodes = n * [None]

        dist = n * [Infinite]
        dist[root] = 0.0
        
        for i in range(n):
            if i == root:
                nodes[i] = pq.insert(i, 0.0)
            else:
                nodes[i] = pq.insert(i, Infinite)
        if Dump:
            print "Priority queue:"
            pq.stampa()
        
        while not pq.isEmpty():
            inode = pq.findMin()
            if Dump:
                print "Extract node", inode
            nodes[inode] = None #marca i nodi gia' visitati
            pq.deleteMin()
            
            curr = g.adj[inode].getFirstRecord()
            while curr != None:
                e = (inode,curr.elem[0],curr.elem[1])
                if nodes[e[1]] != None and dist[e[0]] + e[2] < nodes[e[1]].key:
                    pq.decreaseKey(nodes[e[1]], dist[e[0]] + e[2])
                    
                    if Dump:
                        print "decreaseKey({},{})".format(e[1], dist[e[0]] + e[2])
                        pq.stampa()
                    
                    dist[e[1]] = dist[e[0]] + e[2]
                curr = curr.next
        return dist

    @staticmethod
    def FloydWarshall(g):
        """ Restiruisce una matrice con le distanze punto - punto """
        
        #Inizializzazione
        n = len(g.nodes)
        dist = n * [None]
        
        if Dump:
            print "Initialization. Distances:"
        for i in range(n):
            dist[i] = n * [Infinite]
            dist[i][i] = 0.0
            
            curr = g.adj[i].getFirstRecord()
            while curr != None:
                e = (i,curr.elem[0],curr.elem[1])
                dist[i][e[1]] = e[2]
                curr = curr.next
            if Dump:
                print dist[i]

        for k in range(n):
            if Dump:
                print "Iteration", k
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != Infinite and dist[k][j] != Infinite and dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]    #Watch it!
                        if Dump:
                            print "Update dist({},{}) to dist({},{})+dist({},{})={}".format(i, j, i, k, k, j, dist[i][j])
        
        return dist
        

def buildGraph():
    g = Graph()
    ginfo = ((0, 1, 3.0), (0, 3, 1.0), (1, 3, 2.0), (1, 2, 4.0), (2, 3, 5.0))
    n = []
    for i in range(4):
        n.append(g.insertNode(i))
    for e in ginfo:
        g.insertArc(n[e[0]].index, n[e[1]].index, e[2])
        g.insertArc(n[e[1]].index, n[e[0]].index, e[2])
    return g

if __name__ == "__main__":
    g = buildGraph()
    print "\tThe graph:"
    g.stampa()
    print
    
    print "\tBellmanFordMoore:"
    d = ShortestPaths.BellmanFordMoore(g, 0)
    print "\tDstances:", d
    print
    
    print "\tDijkstra:"
    d = ShortestPaths.Dijkstra(g, 0)
    print "\tDistances:", d
    print
    
    print "\tFloydWarshall:"
    d = ShortestPaths.FloydWarshall(g)
    print "\tDistances:"
    for i in range(len(d)):
        print "\t", d[i]
    print
    

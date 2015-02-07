'''
Created on 21/nov/2014

@author: Francesco
'''
from stack.Stack import PilaArrayList
from queue.Queue import CodaArrayList_deque

class BinaryNode:
    def __init__(self, info):
        self.info = info
        self.father = None
        self.leftSon = None
        self.rightSon = None

class BinaryTree:
    def __init__(self, rootNode=None):
        self.root = rootNode
    
    def insertAsLeftSubTree(self, father, subtree):
        son = subtree.root
        if son != None:
            son.father = father
        father.leftSon = son
    
    def insertAsRightSubTree(self, father, subtree):
        son = subtree.root
        if son != None:
            son.father = father
        father.rightSon = son

    def cutLeft(self, father):
        son = father.leftSon
        newTree = BinaryTree(son)
        father.leftSon = None
        return newTree
    
    def cutRight(self, father):
        son = father.rightSon
        newTree = BinaryTree(son)
        father.rightSon = None
        return newTree

    def DFS(self):
        res = []     
        stack = PilaArrayList()
        if self.root != None:
            stack.push(self.root)
        while not stack.isEmpty():
            current = stack.pop()
            res.append(current.info)
            if current.rightSon != None:
                stack.push(current.rightSon)
            if current.leftSon != None:
                stack.push(current.leftSon)
        return res

    def BFS(self):
        res = []
        q = CodaArrayList_deque()
        if self.root != None:
            q.enqueue(self.root)
        while not q.isEmpty():
            current = q.dequeue()
            res.append(current.info)
            if current.leftSon != None:
                q.enqueue(current.leftSon)
            if current.rightSon != None:
                q.enqueue(current.rightSon)
        return res

    def cut(self, node):
        if node == None:
            return BinaryTree(None)
        if node.father == None:
            return BinaryTree(node)
        f = node.father
        if node.leftSon == None and node.rightSon == None: #a leaf!
            if f.leftSon == node:
                f.leftSon = None
            else:
                f.rightSon = None
            return BinaryTree(node)
        elif node.leftSon != None:
            nt = self.cutLeft(f)
            f.leftSon = None
            return nt
        else:
            nt = self.cutRight(f)
            f.rightSon = None
            return nt

    def stampa(self):
        stack = PilaArrayList()
        if self.root != None:
            stack.push([self.root, 0])
        else:
            print "Empty tree!"
        while not stack.isEmpty():
            current = stack.pop()
            level = current[1]
            print "|---"*level + str(current[0].info)
            
            if current[0].rightSon != None:
                stack.push([current[0].rightSon, level + 1])
            if current[0].leftSon != None:
                stack.push([current[0].leftSon, level + 1])
            level += 1    

if __name__ == "__main__":
        print "alb1=nodo1=1"
        alb1 = BinaryTree(BinaryNode(1))
        nodo1 = alb1.root

        print "alb2=nodo2=2"
        alb2 = BinaryTree(BinaryNode(2))
        nodo2 = alb2.root

        print "alb3=nodo3=3"
        alb3 = BinaryTree(BinaryNode(3));
        nodo3 = alb3.root

        print "alb4=nodo4=4"
        alb4 = BinaryTree(BinaryNode(4))
        nodo4 = alb4.root

        print "alb5=nodo5=5"
        alb5 = BinaryTree(BinaryNode(5))
        nodo5 = alb5.root
        
        print "alb6=nodo6=6"
        alb6 = BinaryTree(BinaryNode(6))
        nodo6 = alb6.root

        print "alb1.innestaDestro(nodo1,alb3)"
        alb1.insertAsRightSubTree(nodo1, alb3)
        print "alb1.innestaSinistro(nodo1,alb2)"
        alb1.insertAsLeftSubTree(nodo1, alb2)
        print "alb1.innestaDestro(nodo3,alb4)"
        alb1.insertAsRightSubTree(nodo3, alb4)
        print "alb1.innestaSinistro(nodo2,alb5)"
        alb1.insertAsLeftSubTree(nodo2, alb5)
        print "alb1.innestaDestro(nodo2,alb6)"
        alb1.insertAsRightSubTree(nodo2, alb6)

        alb1.stampa()

        print "alb1.DFS()"
        visita = alb1.DFS()
        print visita

        print "alb1.BFS()" 
        visita = alb1.BFS()
        print visita
        
        print "alb8=alb1.cutLeft(nodo1)"
        alb8 = alb1.cutLeft(nodo1)
        print "alb1.DFS()"
        visita = alb1.DFS()
        print visita
        print "alb8.DFS()"
        visita = alb8.DFS()
        print visita


'''
Created on 21/nov/2014

@author: Francesco
'''
from trees.binaryTree import BinaryTree
from trees.binaryTree import BinaryNode

class DictBinaryTree:
    def __init__(self):
        self.tree = BinaryTree()
    
    def key(self, node):
        if node == None:
            return None
        return node.info[0]
    
    def value(self, node):
        if node == None:
            return None
        return node.info[1]
    
    def maxKeySon(self, root):
        #go to the right as far as possible!
        curr = root
        while curr.rightSon != None:
            curr = curr.rightSon
        return curr
    
    def isLeftSon(self, node):
        if node == node.father.leftSon:
            return True
        return False
    
    def search(self, key):
        node = self.searchNode(key)
        return self.value(node)
    
    def searchNode(self, key):
        if self.tree.root == None:
            return None
        
        curr = self.tree.root
        while curr != None:
            ck = self.key(curr)
            if key == ck:
                return curr
            
            if key < ck:
                curr = curr.leftSon
            else:
                curr = curr.rightSon
        
        return None
    
    def insert(self, key, value):
        pair = [key, value]
        newt = BinaryTree(BinaryNode(pair))
        
        if self.tree.root == None:
            self.tree.root = newt.root
        else:
            curr = self.tree.root
            pred = None
            while curr != None:
                pred = curr
                if key <= self.key(curr):
                    curr = curr.leftSon
                else:
                    curr = curr.rightSon
            
            if key <= self.key(pred):
                self.tree.insertAsLeftSubTree(pred, newt)
            else:
                self.tree.insertAsRightSubTree(pred, newt)

    def cutOneSonNode(self, node): #contrai un nodo con un singolo figlio
        son = None
        if node.leftSon != None:
            son = node.leftSon
        elif node.rightSon != None:
            son = node.rightSon
        
        if son == None:
            self.tree.cut(node) #is a leaf
        else:
            node.info, son.info = son.info, node.info #swap info
            nt = self.tree.cut(son)
            self.tree.insertAsLeftSubTree(node, nt.cut(son.leftSon))
            self.tree.insertAsRightSubTree(node, nt.cut(son.rightSon))

    def delete(self, key):
        toRemove = self.searchNode(key)
        if toRemove != None:
            if toRemove.leftSon == None or toRemove.rightSon == None:
                self.cutOneSonNode(toRemove)
            else:
                maxLeft = self.maxKeySon(toRemove.leftSon)
                toRemove.info, maxLeft.info = maxLeft.info, toRemove.info
                self.cutOneSonNode(maxLeft)

if __name__ == "__main__":
    diz = DictBinaryTree()
    
    print "insert(6,12)"
    diz.insert(6, 12)
    diz.tree.stampa()
    
    print "insert(4,8)"
    diz.insert(4, 8)
    diz.tree.stampa()
    
    print "insert(3,6)"
    diz.insert(3, 6)
    diz.tree.stampa()
    
    print "insert(2,4)"
    diz.insert(2, 4)
    diz.tree.stampa()
    
    print "insert(1,2)"
    diz.insert(1, 2)
    diz.tree.stampa()
    
    print "insert(5,10)"
    diz.insert(5, 10)
    diz.tree.stampa()
    
    print "insert(7,14)"
    diz.insert(7, 14)
    diz.tree.stampa()
    
    print "search(5)=" + str(diz.search(5))
    print "search(3)=" + str(diz.search(3))
    print "search(6)=" + str(diz.search(6))
    print "search(8)=" + str(diz.search(8))
    
    print "delete(6)"
    diz.delete(6)
    diz.tree.stampa()
    
    print "delete(3)"
    diz.delete(3)
    diz.tree.stampa()
    
    print "delete(1)"
    diz.delete(1)
    diz.tree.stampa()
    
    print "delete(8)"
    diz.delete(8)
    diz.tree.stampa()


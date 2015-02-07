class record:
    def __init__(self,elem):
        self.elem=elem
        self.next=None
        self.index=None
        self.prev=None
class doubleLinkedList:
    def __init__(self):
        self.first=None
        self.last=None
    def addFirst(self,elem):
        rec=record(elem)
        if self.first==None:
            self.first=self.last=rec
            rec.index=0
        else:
            rec.next=self.first
            self.first.prev=rec
            a=self.first
            while a.next!=None:
                a.index=a.index+1
                a=a.next
            self.last.index=self.last.index+1
            self.first=rec
            self.first.index=0
    def addLast(self,elem):
        rec=record(elem)
        if self.first==None:
            self.first=self.last=rec
            rec.index=0
        else:
            self.last.next=rec
            rec.prev=self.last
            rec.index=self.last.index+1
            self.last=rec
    def printList(self):
        if self.first==None:
            print '[]'
        else:
            s='['
            rec=self.first
            while rec.next!=None:
                s=s+str(rec.elem)+', '
                s=s+str(self.last.elem)+']'
            print s
    def printelem(self,index):
        if index>self.last.index:
            print 'error, the index your searching is too high'
        if index<0:
            print 'invalid syntax, the index must be a Natural number'
        rec=self.first
        while rec.index!=index:
            rec=rec.next
        print rec.elem
    
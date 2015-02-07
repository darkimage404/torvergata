
class DictionaryOrderedArrayList:
    def __init__(self):
        self.theList = []
    
    def insert(self, key, value):
        pair = [key, value]
        if len(self.theList) == 0:
            self.theList.append(pair)
        else:
            #find the right position for the new element to keep the array ordered
            currPos = 0
            while currPos < len(self.theList) and self.theList[currPos][0] < key:
                currPos += 1
            if currPos >= len(self.theList):
                self.theList.append(pair)
            else:
                self.theList.insert(currPos, pair)
    
    def delete(self, key):
        res = self.binarySearch(key)
        if res != None:
            pos = res[1]
            del self.theList[pos]
    
    def binarySearch(self, k):
        left = 0
        right = len(self.theList)
        while right - left > 0:
            middle = (left + right) / 2
            midPair = self.theList[middle]
            midKey = midPair[0] #0 is the key, 1 is the value
            midValue = midPair[1]
            if k == midKey:
                return midValue, middle
            if k < midKey:
                right = middle
            else:
                left = middle + 1        
        return None

if __name__=="__main__":
    print "Dictionary (ordered arraylist)."
    d=DictionaryOrderedArrayList()
    print "insert({},{})".format(0,10)
    d.insert(0,10)
    print "insert({},{})".format(2,12)
    d.insert(2,12)
    print "insert({},{})".format(1,11)
    d.insert(1,11)
    print "insert({},{})".format(8,18)
    d.insert(8,18)
    print "insert({},{})".format(5,15)
    d.insert(5,15)
    
    print d.theList
    
    print "delete({})".format(0)
    d.delete(0)
    
    print d.theList
    
    print "binarySearch({})".format(5)
    print d.binarySearch(5)[0]
    
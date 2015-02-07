
class Node:
    def __init__(self, index, elem,weight=None):
        self.index = index
        self.elem = elem
        self.weight=weight #Not always used

class Arc:
    def __init__(self, tail, head, weight=None):
        self.head = head #index
        self.tail = tail #index
        self.weight = weight #Not always used

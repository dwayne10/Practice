class Deque:
    '''
    In this version of Deque,
    Rear is considered the first element of the list i.e array element 0
    Front is considered the last element of the list i.e array element
    len(array)

    For eg: if the deque is 	[8.4,'dog',4,'cat',True]
    8.4 is the Rear and True is the Front

    Therefore adding and removing items from the front is O(1) whereas
    adding and removing from the rear is O(n).

    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, val):
        self.items.insert(0,val)

    def addFront(self,val):
        self.items.append(val)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return  self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
print(d.isEmpty())
d.addRear(4)
print(d)

d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())
print(d)
print(d.isEmpty())
d.addRear(8.4)
d.removeRear()
d.removeFront()

from pythonds.basic.deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
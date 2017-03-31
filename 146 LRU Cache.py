class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import deque
        self.cap = capacity
        self.map = {}
        self.q = LinkedList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            # move to front of q
            # return value
            val = self.map[key].val
            self.q.delete(self.map[key])
            self.q.insert(key, val)  # moves it to front
            self.map[key] = self.q.head
            return val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            # set the existing value to input value
            # then move it to front of q

            # node = self.map[key]
            self.q.delete(self.map[key])
            self.q.insert(key, value)

        else:
            if len(self.map) == self.cap:
                # max capacity reached. Remove last element in q
                print(self.q.tail.key)

                del self.map[self.q.tail.key]
                self.q.delete(self.q.tail)
            self.q.insert(key, value)
        self.map[key] = self.q.head


class Node(object):
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = None
        self.prev = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key, val):
        node = Node(key, val)
        if self.head:
            node.next = self.head
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def delete(self, node):

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            # last node
            self.tail = node.prev

        del node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
obj.get(2)
obj.put(1,1)
obj.put(4,1)
obj.get(2)

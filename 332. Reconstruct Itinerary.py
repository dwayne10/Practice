class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets.sort(key=lambda x: x[1])

        g = Graph()
        for t in tickets:
            g.addedge(t[0], t[1])

        return g.topologicalSort()


class Graph:

    def __init__(self):

        from collections import defaultdict
        self.graph = defaultdict(list)

    def addedge(self, u, v):
        self.graph[u].append(v)

    def topoUtil(self, label):

        while self.graph[label]:
            next_node = self.graph[label].pop(0)  # critical step - remove it from its neighbors
            self.topoUtil(next_node)

        self.stack.insert(0, label)

    def topologicalSort(self):

        self.stack = []
        self.topoUtil("JFK")
        return self.stack

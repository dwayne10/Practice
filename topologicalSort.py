from collections import defaultdict


class Graph:
    def __init__(self, num_of_vertices):
        self.graph = defaultdict(list)
        self.V = num_of_vertices

    def addEdge(self, source, dest):
        self.graph[source].append(dest)

    def __topologicalSortUtil(self, u, visited, stack):
        visited[u] = True
        for v in self.graph[u]:
            if visited[v] is False:
                self.__topologicalSortUtil(v, visited, stack)
        stack.insert(0, u)

    def topologicalSort(self):

        visited = [False] * self.V
        stack = []

        for node in range(self.V):
            if visited[node] is False:
                self.__topologicalSortUtil(node, visited, stack)

        print(stack)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topologicalSort()

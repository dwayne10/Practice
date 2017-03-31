from collections import defaultdict


class Graph:
    def __init__(self, num_of_vertices):
        self.V = num_of_vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCycleInDFS(self, u, visited, recursive_stack):

        visited[u] = True
        recursive_stack[u] = True

        for v in self.graph[u]:
            if recursive_stack[v] is True:
                return True
            if not visited[v]:
                if self.isCycleInDFS(v, visited, recursive_stack):
                    return True

        recursive_stack[u] = False
        return False

    def isCyclePresent(self):

        if not self.graph:
            return False

        visited = [False] * self.V
        recursive_stack = [False] * self.V

        # Call the recursive helper function to detect cycle in different
        # DFS trees
        for i in range(self.V):
            if visited[i] is False:
                if self.isCycleInDFS(i, visited, recursive_stack) is True:
                    return True
        return False


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(4, 1)
g.addEdge(3, 2)
g.addEdge(3, 1)
print(g.isCyclePresent())

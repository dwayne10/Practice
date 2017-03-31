from collections import defaultdict


class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = Graph(numCourses)

        for u, v in prerequisites:
            g.addEdge(u, v)

        if g.isCyclePresent():
            return False  # cannot take courses as there is a cycle
        return True


class Graph:

    def __init__(self, num_of_vertices):
        self.V = num_of_vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def checkIfCycleInDFS(self, u, visited, stack):

        visited[u] = True
        stack[u] = True

        for v in self.graph[u]:
            if stack[v] is True:
                return True
            if visited[v] is False:
                if self.checkIfCycleInDFS(v, visited, stack) is True:
                    return True

        stack[u] = False
        return False

    def isCyclePresent(self):

        visited = [False] * self.V
        stack = [False] * self.V

        for i in range(self.V):
            if visited[i] is False:
                if self.checkIfCycleInDFS(i, visited, stack) is True:
                    return True
        return False

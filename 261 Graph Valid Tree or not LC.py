class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        def add_edge(u, v):
            g[u].append(v)
            g[v].append(u)

        def isCycleThere(source, parent):
            visited[source] = True

            for neighbor in g[source]:
                if visited[neighbor] == False:
                    if isCycleThere(neighbor, source):
                        return True
                elif visited[neighbor] == True and neighbor != parent:
                    return True
            return False

        from collections import defaultdict
        g = defaultdict(list)
        for u, v in edges:
            add_edge(u, v)

        visited = [False] * n
        if isCycleThere(0, -1):
            return False  # i.e not a valid tree
        else:
            if visited.count(False) != 0:
                return False  # one or more nodes not visited. So its not a valid tree
            else:
                return True
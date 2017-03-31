# Definition for a undirected graph node
class UndirectedGraphNode:

    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneGraph(self, orig_root):
        if not orig_root:
            return None
        if not orig_root.neighbors:
            a = UndirectedGraphNode(orig_root.label)
            return a

        vertex_map = {}
        # create new node from given input
        copy_root = UndirectedGraphNode(orig_root.label)

        q = []
        q.append(orig_root)  # add the original input node to the Q

        # map from original root to new clone graph's node
        vertex_map[orig_root] = copy_root

        # perform BFS
        while len(q) >= 1:
            u = q.pop()

            for v in u.neighbors:
                if v not in vertex_map:
                    # Create a new node and map it to v
                    vertex_map[v] = UndirectedGraphNode(v.label)
                    q.append(v)

                # below line translate into copy_of_u.neighbors.append(v) . We
                # are not actually returning the vertex map
                # the outputs of the map are used to link the nodes together!

                # below we cannot do append(v) as that would point back to the original nodes
                # we have to do append(vertex_map[v]) as that would point to
                # the copy
                vertex_map[u].neighbors.append(vertex_map[v])

                # i.e add this node as a neighbor of the copy node
                # vertex_map[u] = copy_of_u

        # -> this gives the root of the graph clone
        return vertex_map[orig_root]

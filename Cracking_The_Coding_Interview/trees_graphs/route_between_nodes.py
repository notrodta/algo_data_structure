#Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.


#answer, can use either dfs or bfs
# bfs can help find shortest path
# dfs is easier to implement



'''         ANOTHER WAY    '''

from collections import defaultdict
from collections import deque


# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # Use BFS to check path between s and d

    def isReachable(self, s, d):
        visited = set()
        q = deque([])
        q.append(s)
        visited.add(s)

        while q:
            curr = q.popleft()
            if curr == d:
                return True
            for i in self.graph[curr]:
                if i not in visited:
                    q.append(i)
                    visited.add(i)

        return False







# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

u = 1
v = 3

if g.isReachable(u, v):
    print("There is a path from %d to %d" % (u, v))
else:
    print("There is no path from %d to %d" % (u, v))





    '''               ANOTEH WAY  (GOOOD WAY!)    '''


# graph is here: https://www.youtube.com/watch?v=bs2er-CleeI
graph = {0:[1,2],
         1: [2,3],
         2: [3],
         3: [4,5],
         4: [5],
         5: []}


def alt_ans(graph, s,d):
    visited = set()
    q = deque([])

    visited.add(s)
    q.append(s)

    while q:
        curr = q.popleft()
        if curr == d:
            return True
        for node in graph[curr]:
            if node not in visited:
                q.append(node)
                visited.add(node)

    return False

print(alt_ans(graph, 0,3))
print(alt_ans(graph, 3,0))
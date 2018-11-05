#https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/


#DFS AND BFS both time complexity is O(V+E)

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


print(graph['B'])
print(type(graph))



def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print("before stack:", stack)
            stack.extend(graph[vertex] - visited) # deleting visited from graph. Graph is a dictionary, this only works with a dictionary
            print("after stack:", stack)
            print()
    return visited

print(dfs(graph, 'A'))


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited) # only works with dictionary
    return visited

print(bfs(graph, 'A'))



'''         MORE CLEAR WAY      '''


from collections import deque
def bfs(root):
    queue = deque([])
    root.marked = True
    queue.append(root)

    while(len(queue) > 0):
        r = queue.popleft()
        print(r)
        for node in r.adjacent:
            if node.marked == False:
                node.marked = True
                queue.append(node)


#pseudo
def dfs(root):
    if root == None: return
    print(root)
    root.visited = True

    for node in root.adjacent:
        if node.visited == False:
            dfs(node)

# this works, this code is assuming node dont have visited attribute
def dfs_better(root, visited = set()):
    if root is None: return

    print(root.data)

    for node in get_neigbhor(root):
        if node not in visited:
            visited.add(node)
            dfs_better(node, visited)


def get_neigbhor(root):
    l = []
    if root.left:
        l.append(root.left)
    if root.right:
        l.append(root.right)

    return l




from bst import Node
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print("dfs_better:")
dfs_better(root)


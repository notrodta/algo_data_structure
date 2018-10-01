#https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print(dfs(graph, 'A'))


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print(bfs(graph, 'A'))


#pseudo
def dfs(root):
    if root == None: return
    print(root)
    root.visited = True

    for node in root.adjacent:
        if node.visited == False:
            dfs(node)


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













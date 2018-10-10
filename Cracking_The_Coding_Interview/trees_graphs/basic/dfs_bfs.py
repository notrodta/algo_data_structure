#https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

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




#Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.


#answer, can use either dfs or bfs
# bfs can help find shortest path
# dfs is easier to implement

def check_if_path_found(dest, curr):
    if dest == curr:
        return True
    return False


from collections import deque
def bfs(root, dest):
    queue = deque([])
    root.marked = True
    queue.append(root)

    while(len(queue) > 0):
        r = queue.popleft()
        if check_if_path_found(dest, r): return True
        for node in r.adjacent:
            if node.marked == False:
                node.marked = True
                queue.append(node)

    return False



def dfs(root,dest):
    if root == None: return
    if check_if_path_found(dest, root): return True
    root.visted = True

    for node in root.adjacent:
        if node.visited == False:
            dfs(node)





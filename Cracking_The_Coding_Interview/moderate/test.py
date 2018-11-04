def dfs(root):
    if root == None: return
    print(root)
    root.visited = True

    for node in root.adjacent:
        if node.visited == False:
            dfs(node)
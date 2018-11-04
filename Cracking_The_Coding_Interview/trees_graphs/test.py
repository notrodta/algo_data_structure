from basic.bst import Node


# sum = 0

def dfs(root, sum = [0], sum_t = "s", visited = set(), temp = []):
    if root is None: return

    print(temp, sum, sum_t)

    print(root.data)
    #global sum
    sum[0] += 1
    sum_t += "s"

    for node in get_neigbhor(root):
        if node not in visited:
            visited.add(node)
            temp.append(node.data)
            dfs(node, sum, sum_t, visited, temp)

    return "sum: " + str(sum) + "sum_t:" + str(sum_t)
    #return temp




def get_neigbhor(root):
    l = []
    if root.left:
        l.append(root.left)
    if root.right:
        l.append(root.right)

    return l


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print(dfs(root))
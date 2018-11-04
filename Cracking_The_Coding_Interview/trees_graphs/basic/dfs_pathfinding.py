from bst import Node

'''
variable revert back 1 step after return
arr in parameter stays the same even after return function, unless you return that arr, then the arr go back 1 step

'''

def get_children(root):
    l = []
    if root.left:
        l.append(root.left)
    if root.right:
        l.append(root.right)
    return l

# # not the shortest, just return the first path found
# def answer(root, end, path=[]):
#     path = path + [root.data]
#     print(path)
#
#     if root.data == end:
#         return path
#
#     for node in get_children(root):
#         if node.data not in path:
#             newPath = answer(node, end, path)
#             if newPath != None:
#                 return newPath
#
#     return None


# testing
# not the shortest, just return the first path found
def answer(root, end, path = []):
    if root is None: return

    print(path)


    for node in get_children(root):
        if node not in path:
            path = path + [root.data]
            answer(node, end, path)




def shortest_path_dfs(root, end, path=[], shortest= None):
    path = path + [root.data]

    if root.data == end:
        return path

    for node in get_children(root):
        if node not in path:
            if shortest is None or len(path) < len(shortest):
                newpath = shortest_path_dfs(node, end, path, shortest)
                if newpath != None:
                    shortest = newpath
                    
    return shortest



root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
y = root.right.right = Node(10)
x = root.left.left.left = Node(10)

print(answer(root, 5))
# print(answer(root, 10))
print()
print(shortest_path_dfs(root, 10))





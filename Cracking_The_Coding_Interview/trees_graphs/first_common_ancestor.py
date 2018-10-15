# First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.


#https://www.youtube.com/watch?v=GnliEfQo114

from basic.bst import Node
from collections import deque

def get_children(root):
    l = []
    if root.left:
        l.append(root.left)
    if root.right:
        l.append(root.right)
    return l


# dfs pathfinding for shortest path
def path_to_x(start, end, path=[], shortest = None):
    path = path + [start.data]

    if start.data == end:
        return path

    for node in get_children(start):
        if node not in path:
            if shortest is None or len(path) < len(shortest):
                new_path = path_to_x(node, end, path, shortest)
                if new_path != None:
                    shortest = new_path

    return shortest


def answer(root, node1, node2):
    n1 = path_to_x(root, node1)
    n2 = path_to_x(root, node2)

    q1 = deque(n1)
    q2 = deque(n2)

    curr = ""
    while len(q1) > 0 and len(q2) > 0:
        x = q1.popleft()
        y = q2.popleft()
        if x == y:
            curr = x
        else:
            break

    return curr





root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print(answer(root, 1, 3))
print(answer(root, 1, 7))




# Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.


#https://www.youtube.com/watch?v=kzycaQ2YOdw
from basic.bst import Node


# O(n)  just inorder traversal
def inorder(root,n, arr):
    if len(arr) >= 2:
        return

    if root:
        inorder(root.left, n, arr)
        if len(arr) > 0 and len(arr) < 2:
            arr.append(root.data)
        if root.data == n:
            arr.append(root.data)
        inorder(root.right,n, arr)

def answer(root, n):
    arr = []
    inorder(root,n, arr)
    if len(arr) == 2:
        return arr[1]
    return None




root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)


print(answer(root, 1))
print(answer(root, 2))
print(answer(root, 3))
print(answer(root, 4))
print(answer(root, 5))
print(answer(root, 6))
print(answer(root, 7))




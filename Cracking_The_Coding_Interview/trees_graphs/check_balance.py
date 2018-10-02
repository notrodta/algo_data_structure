# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never di er by more than one.


# tutorial: https://www.youtube.com/watch?v=nOcFiGl5Vy4
from basic.bst import Node


def is_balanced(root):
    return is_balanced_height(root) >= 0


def is_balanced_height(root):
    if root is None: return 0

    left = is_balanced_height(root.left)
    right = is_balanced_height(root.right)

    if left < 0 or right < 0: return -1
    if abs(left - right) > 1: return -1

    return max(left, right) + 1


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)


print(is_balanced(root))

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)


print(is_balanced(root))























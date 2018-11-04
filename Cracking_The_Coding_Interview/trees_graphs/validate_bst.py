# Validate BST: Implement a function to check if a binary tree is a binary search tree.



# Python program to check if a binary tree is bst or not

INT_MAX = 4294967296
INT_MIN = -4294967296


# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Min Max Method
def is_bst(root):
    return is_bst_helper(root, INT_MIN, INT_MAX)


def is_bst_helper(node, mini, maxi):
    if node is None:
        return True

    if node.data <= mini or node.data > maxi:
        return False

    return is_bst_helper(node.left, mini, node.data) and is_bst_helper(node.right, node.data, maxi)

# InOrder Method with array
def is_bst_inorder_array_helper(root, arr):
    if root is None:
        return True

    is_bst_inorder_array_helper(root.left, arr)
    arr.append(root.data)
    is_bst_inorder_array_helper(root.right, arr)
    return arr

def is_bst_inorder_array(root):
    arr = is_bst_inorder_array_helper(root, [])

    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            return False

    return True


# InORder without array (better than with array)
prev = None
def is_bst_inorder(root):
    if root is None:
        return True

    if is_bst_inorder(root.left) is False: return False

    global prev

    #print(prev, root.data)

    if prev is not None and root.data < prev: return False
    prev = root.data

    if is_bst_inorder(root.right) is False: return False

    return True










root1 = Node(3)
root1.left = Node(3)
root1.right = Node(6)
root1.left.left = Node(1)

if (is_bst(root1)):
    print("Is BST")
else:
    print("Not a BST")

print(is_bst_inorder_array(root1))
print(is_bst_inorder(root1))
print()

# from basic.tree_traversal import *
# inOrder(root1)






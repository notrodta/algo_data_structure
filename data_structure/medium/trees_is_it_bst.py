'''
Q: Check to see if tree is binary search tree



When to use Pre-Order, In-order or Post-Order?
The traversal strategy the programmer selects depends on the specific needs of the algorithm being designed.
The goal is speed, so pick the strategy that brings you the nodes you require the fastest.

If you know you need to explore the roots before inspecting any leaves, you pick pre-order because you will
encounter all the roots before all of the leaves.

If you know you need to explore all the leaves before any nodes, you select post-order because you don't waste any
time inspecting roots in search for leaves.

If you know that the tree has an inherent sequence in the nodes, and you want to flatten the tree back into its
original sequence, than an in-order traversal should be used. The tree would be flattened in the same way it was created. A pre-order or post-order traversal might not unwind the tree back into the sequence which was used to create it.




resources:
https://stackoverflow.com/questions/9456937/when-to-use-preorder-postorder-and-inorder-binary-search-tree-traversal-strate

preorder = root left right
inorder = left root right
postorder = left right root

'''

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

l = []


def checkBST(root):
    get_inorder(root)

    for i in range(0, len(l) - 1):
        if l[i] >= l[i + 1]:
            return False
    return True


# used inorder. Need to review pro order, post order, and in order
def get_inorder(root):
    if root is None:
        return
    get_inorder(root.left)
    l.append(root.data)
    get_inorder(root.right)



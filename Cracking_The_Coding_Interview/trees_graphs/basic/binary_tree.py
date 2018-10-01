from tree_traversal import inOrder, preOrder, postOrder

# binary tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        return None





root = Node(10)
root.left = Node(5)
root.right= Node(3)


inOrder(root)

#all O(n)

def inOrder(node):
    if node != None:
        inOrder(node.left)
        print(node.data)
        inOrder(node.right)


def preOrder(node):
    if node != None:
        print(node.data)
        preOrder(node.left)
        preOrder(node.right)


def postOrder(node):
    if node != None:
        postOrder(node.left)
        postOrder(node.right)
        print(node.data)


from bst import Node

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

inOrder(root)
print()
preOrder(root)
print()
postOrder(root)
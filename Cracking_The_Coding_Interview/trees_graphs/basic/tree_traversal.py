def inOrder(node):
    if node != None:
        inOrder(node.left)
        print(node.data)
        inOrder(node.right)


def preOrder(node):
    if node != None:
        print(node)
        preOrder(node.left)
        preOrder(node.right)


def postOrder(node):
    if node != None:
        postOrder(node.left)
        postOrder(node.right)
        print(node)
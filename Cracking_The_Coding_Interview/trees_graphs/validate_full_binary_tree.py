class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

def ans(root):
    level = []
    level.append(root)

    while level:
        temp = []
        for node in level:
            l = []
            if node.left:
                temp.append(node.left)
                l.append(node.left)
            if node.right:
                temp.append(node.right)
                l.append(node.right)
            if len(l) == 1:
                return False
        level = temp


    return True


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
print(ans(root))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
# root.left.right.right = Node(7)
print(ans(root))
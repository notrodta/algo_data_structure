# Given a binary tree, get the most left node of each level

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


def traverse_tree(root):
    if root is None:
        return

    levels = []
    q = [root]
    levels.append([root])

    while q:
        temp = []
        for i in q:
            if i.left:
                temp.append(i.left)
            if i.right:
                temp.append(i.right)
        if temp: levels.append(temp)
        q = temp

    for i in levels:
        print(i[0])







if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    traverse_tree(root)
    print()

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)
    root.left.right.right.right.left = Node(8)

    traverse_tree(root)
    print()

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(5)
    root.right.right.right = Node(6)
    root.right.right.right.right = Node(7)
    root.right.right.right.right.left = Node(8)

    traverse_tree(root)

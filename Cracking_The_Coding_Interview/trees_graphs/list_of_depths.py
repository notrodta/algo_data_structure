# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).



# A Binary Tree node
class Node:
    # Constructor to initialise node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

# linked list node
class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data.data)


# gets the node data of every depth
def list_of_depths(root):
    if root is None:
        return []

    depth = []
    q = []
    q.append(root)
    depth.append([root])

    while q:
        temp = []

        for node in q:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

        if len(temp) > 0: depth.append(temp)
        q = temp

    return depth

# prints linked list
def print_linked_list(head):
    curr = head
    s = ""
    while curr:
        s += curr.__str__()
        if curr.next: s += " -> "
        curr = curr.next
    print(s)


# creates linked list from list of node data
def create_linked_list(list): # list of all the nodes on the current depth
    head = ListNode(list[0])
    curr = head

    if len(list) > 1:
        for i in range(1, len(list)):
            curr.next = ListNode(list[i])
            curr = curr.next

    return head


# prints out all the linked list from every depth
def get_all_link_list(depth):
    l = [] # contains the head of each linked list from different depth
    for i in depth:
        ll_head = create_linked_list(i)
        l.append(ll_head)

    for head in l:
        print_linked_list(head)


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    get_all_link_list(list_of_depths(root))

    # for depth, list_nodes in enumerate(list_of_depths(root)):
    #     print('Depth', depth, end=': ')
    #     for n in list_nodes:
    #         print(n.data, end=' -> ')
    #     print('end')




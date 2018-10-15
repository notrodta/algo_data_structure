#from tree_traversal import inOrder, preOrder, postOrder

#https://www.laurentluce.com/posts/binary-search-tree-library-in-python/

class Node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        """
        Node constructor

        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data


    # a new node is always inserted at the leaf
    def insert(self, data):
        """
        Insert new node with data

        @param data node data object to insert
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    '''
    
    DELETING NODE
    
    Node to be deleted is leaf: Simply remove from the tree.
              50                            50
           /     \         delete(20)      /   \
          30      70       --------->    30     70 
         /  \    /  \                     \    /  \ 
       20   40  60   80                   40  60   80
       
    Node to be deleted has only one child: Copy the child to the node and delete the child
             50                            50
           /     \         delete(30)      /   \
          30      70       --------->    40     70 
            \    /  \                          /  \ 
            40  60   80                       60   80
            
    Node to be deleted has two children: Find inorder successor of the node. Copy contents of the inorder successor to the node and delete the inorder successor. Note that inorder predecessor can also be used.
    
              50                            60
           /     \         delete(50)      /   \
          40      70       --------->    40    70 
                 /  \                            \ 
                60   80                           80
    
    '''

    # Given a binary search tree and a key, this function
    # delete the key and returns the new root
    def deleteNode(root, key):

        # Base Case
        if root is None:
            return root

            # If the key to be deleted is smaller than the root's
        # key then it lies in  left subtree
        if key < root.key:
            root.left = deleteNode(root.left, key)

            # If the kye to be delete is greater than the root's key
        # then it lies in right subtree
        elif (key > root.key):
            root.right = deleteNode(root.right, key)

            # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

                # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = deleteNode(root.right, temp.key)

        return root

    def lookup(self, data, parent=None):
        """
        Lookup node containing data

        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent


    def print_tree(self): #inorder
        """
        Print tree content inorder
        """
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def __str__(self):
        return str(self.data)


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

node, parent = root.lookup(6)
#print(node.data, parent.data)



# code from hackerrank
# https://www.hackerrank.com/challenges/tree-inorder-traversal/problem?h_r=internal-search

'''
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                    
                    '''



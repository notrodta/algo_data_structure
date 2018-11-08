# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.


#from basic.bst import *



class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def print_tree(self): # inorder
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()




# bst = left < parent < right
# O(log n)? <- same as binary search
def answer(list, start, end):
    if len(list) < 0: return None
    if end < start: return

    mid = (start+end)//2
    root = Node(list[mid])

    root.left = answer(list, start, mid-1)
    root.right = answer(list, mid+1, end)

    return root


l = [1,2,3,4,5,6,7]
tree = answer(l,0,len(l)-1)
tree.print_tree()

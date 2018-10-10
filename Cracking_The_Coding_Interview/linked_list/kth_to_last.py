# Return Kth to Last: Implement an algorithm to  nd the kth to last element of a singly linked list.

from basic.single_linked_list import *

def answer(head, k):
    curr = head
    ahead = head
    for i in range(0,k):
        ahead = ahead.next

    while ahead:
        curr = curr.next
        ahead = ahead.next

    return curr.data


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(6)
node.next.next.next.next.next.next = ListNode(7)
node.next.next.next.next.next.next.next = ListNode(8)
node.next.next.next.next.next.next.next.next = ListNode(9)

print_list(node)
print()

print(answer(node,3))
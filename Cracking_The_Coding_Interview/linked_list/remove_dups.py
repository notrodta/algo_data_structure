# Remove Dups: Write code to remove duplicates from an unsorted linked list.

from basic.single_linked_list import *

def answer(head):
    s = set()

    prev = head
    curr = prev.next

    while curr is not None:
        if curr.data not in s:
            s.add(curr.data)
            prev.next = curr
            prev = curr
        curr = curr.next
        if curr is None:
            prev.next = curr

    return head



node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(2)
node.next.next.next = ListNode(2)
node.next.next.next.next = ListNode(3)
node.next.next.next.next.next = ListNode(3)
node.next.next.next.next.next.next = ListNode(3)
node.next.next.next.next.next.next.next = ListNode(4)
node.next.next.next.next.next.next.next.next = ListNode(4)

print_list(node)

ans = answer(node)
print()
print_list(ans)


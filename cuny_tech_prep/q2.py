'''

linked list:
design function
root - parameter
remove all node with even value

'''


def delete_even_value_noeds(head):
    while head.data % 2 == 0:
        head = head.next
        if head is None:
            return head

    prev = head
    cur = prev.next

    while cur is not None:
        while cur.data % 2 == 0:
            cur = cur.next
            prev.next = cur
            if cur is None: return head
        if cur.data % 2 != 0:
            prev = cur
            cur = cur.next

    return head
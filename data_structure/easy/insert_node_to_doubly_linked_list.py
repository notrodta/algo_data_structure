# Given a reference to the head of a doubly-linked list and an integer, data, create a new DoublyLinkedListNode object having data value data and insert it into a sorted linked list while maintaining the sort.


def sortedInsert(head, data):
    new = DoublyLinkedListNode(data)
    curr = head

    if head == None:
        head = new
        return head

    if head.data > data:
        head = new
        new.next = curr
        return head

    while curr != None:
        if curr.data >= data:
            new.prev = curr.prev
            curr.prev.next = new
            curr.prev = new
            new.next = curr
            return head
        if curr.next == None:
            if curr.data < data:
                curr.next = new
                new.prev = curr
                curr = new
        curr = curr.next

    return head

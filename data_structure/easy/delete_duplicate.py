# You're given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete as few nodes as possible so that the list does not contain any value more than once. The given head pointer may be null indicating that the list is empty.

def removeDuplicates(head):
    curr = head
    front = head.next

    while front != None:
        if curr.data != front.data:
            curr.next = front
            curr = front

        front = front.next

    curr.next = front

    return head
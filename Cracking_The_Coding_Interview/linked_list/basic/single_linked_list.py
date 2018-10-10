class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def print_list(self):
        self.curr = self.head
        while self.curr:
            print(self.curr.data)
            self.curr = self.curr.next


def print_list(head):
    curr = head

    while curr:
        print(curr.data)
        curr = curr.next




node = ListNode(1)
node.next = ListNode(2)
tail = node.next.next = ListNode(10)
single_linked_list = SingleLinkedList()
single_linked_list.head = node
single_linked_list.tail = tail

# single_linked_list.print_list()
# print(single_linked_list.head.data)
# print(single_linked_list.tail.data)



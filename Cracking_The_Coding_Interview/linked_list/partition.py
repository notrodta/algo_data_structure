# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list the values of x only need to be a er the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.


from basic.single_linked_list import *

#O(n)
def answer(root, n):
    small = None
    small_curr = small

    big = None
    big_curr = big

    while root is not None:
        if root.data < n:
            if small is None:
                small = root
                small_curr = small
            else:
                small_curr.next = root
                small_curr = root
        else:
            if big is None:
                big = root
                big_curr = big
            else:
                big_curr.next = root
                big_curr = root

        root = root.next

    big_curr.next = None
    small_curr.next = big

    return small



root = ListNode(3)
root.next = ListNode(5)
root.next.next = ListNode(8)
root.next.next.next = ListNode(5)
root.next.next.next.next = ListNode(10)
root.next.next.next.next.next = ListNode(2)
root.next.next.next.next.next.next = ListNode(1)

ans = answer(root,5)
print_list(ans)


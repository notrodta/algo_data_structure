'''

A linked list is said to contain a cycle if any node is visited more than once while traversing the list.

Complete the function provided in the editor below. It has one parameter: a pointer to a Node object named 'head' that points
to the head of a linked list. Your function must return a boolean denoting whether or not there is a cycle in the list.
If there is a cycle, return true; otherwise, return false.
'''

'''

also check out the hare and tourtoist solution:
https://www.youtube.com/watch?v=FkBm3NeWqak

'''

def has_cycle(head):
    curr = head
    seen = set()
    while curr:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next
    return False


#solution 2
def has_cycle_two(head):
    node_freq = {}

    curr = head

    while curr != None:
        if curr in node_freq:
            return True

        node_freq[curr] = 1
        curr = curr.next

    return False

# solution 3: hare and tortoise
def has_cycle_three(head):
    tortoise = head
    hare = head

    while hare.next != None:
        if hare == tortoise:
            return True

        hare = hare.next
        tortoise = tortoise.next.next

    return False
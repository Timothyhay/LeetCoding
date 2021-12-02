# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


def reverseList(head):
    crt = head
    pre = None
    nxt = None
    while crt is not None:
        nxt = crt.next
        crt.next = pre
        pre = crt
        crt = nxt
    return pre


def reorderList(self):
    if self.head is None or self.head.next is None:
        return

    # 1) Find the middle point using tortoise and hare
    fast = self.head.next
    slow = self.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # 2) Split the linked list in two halves
    # node1, head of first half    1 -> 2 -> 3
    # node2, head of second half   4 -> 5
    right = slow.next
    left = self.head
    # Remember to add the final None for right linklist!
    slow.next = None

    # 3) Reverse the second half, i.e., 5 -> 4
    right = reverseList(right)

    # 4) Merge alternate nodes
    self = node(0) #Assign a dummy node and make it in-place
    crt = self

    while left is not None or right is not None:
        # First add the element from first list
        if left is not None:
            crt.next = left
            left = left.next
            crt = crt.next
        # Then add the element from second list
        if right is not None:
            crt.next = right
            right = right.next
            crt = crt.next

    # Assign the head of the new list to head pointer
    self = self.next

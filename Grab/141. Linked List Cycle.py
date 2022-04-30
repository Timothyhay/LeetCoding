'''
    Linked List

    node.val may be the same so can not use a hashset
    Use 2 fast&slow pointers. If they meet in the future, hasCicle

    To avoid Nonetype.next exception, check if not slow.next or not fast.next during iteration
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        fast = head
        slow = head
        while slow and fast:
            # Handle Expection
            if not slow.next or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

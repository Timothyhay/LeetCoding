'''
    Linked List

    Use 2 ptr to note the pos of first k-th(n1) and last k-th(n2).
    By iterating(p = p.next) k times(get n1), then set n2 as head pos and iterate to the end.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        n1 = None
        n2 = None

        while p:
            k -= 1
            # When found n1 (idx == k), start to move n2
            # Put it before <check if found n1>
            if n2:
                n2 = n2.next
            # check if found n1
            if k == 0:
                n1 = p
                n2 = head
            p = p.next

        n2.val, n1.val = n1.val, n2.val
        return head


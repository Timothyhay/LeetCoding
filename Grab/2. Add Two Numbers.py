'''
    Linked List

    The traversing order is adding order.
    Remember to check the final carry as new digit if it has one. Like:

    Input:
        [9,9,9,9,9,9,9]
        [9,9,9,9]
    Output: // If forgot final carry
        [8,9,9,9,0,0,0]
    Expected:
        [8,9,9,9,0,0,0,1]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carrier = 0
        p1 = l1
        p2 = l2
        ans = ListNode()
        curr = ans
        while p1 and p2:
            newNode = ListNode()
            curr.next = newNode
            curr = curr.next

            curr.val = (p1.val + p2.val + carrier) % 10
            carrier = (p1.val + p2.val + carrier) // 10

            p1 = p1.next
            p2 = p2.next

        if p1:
            left = p1
        else:
            left = p2

        while left:
            newNode = ListNode()
            curr.next = newNode
            curr = curr.next

            curr.val = (left.val + carrier) % 10
            carrier = (left.val + carrier) // 10
            left = left.next

        if carrier > 0:
            newNode = ListNode()
            curr.next = newNode
            curr = curr.next

            curr.val = carrier

        return ans.next

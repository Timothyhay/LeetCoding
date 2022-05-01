'''
    Linked List
    Priority Queue / Divide and Conquer

    After declaring a priority queue, define:

        def lt(self, other):
            return self.val < other.val
        ListNode.__lt__ = lt

    for ListNode. Or it will not know how to compare in the pq.

    Time complexity : O(Nlogk) where k is the number of linked lists.

    The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue.
    But finding the node with the smallest value just costs O(1) time.
    There are N nodes in the final linked list.

    Space complexity :
    O(k) The code above present applies in-place method which cost O(1) space.
    And the priority queue (often implemented with heaps) costs O(k) space (it's far less than N in most situations).

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        q = PriorityQueue()

        def lt(self, other):
            return self.val < other.val
        ListNode.__lt__ = lt

        for l in lists:
            if l:
                q.put((l.val, l))

        while not q.empty():
            val, node = q.get()
            curr.next = node
            curr = curr.next
            if node.next:
                q.put((node.next.val, node.next))

        return head.next

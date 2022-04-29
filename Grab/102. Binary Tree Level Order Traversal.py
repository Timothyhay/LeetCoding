'''
    Binary Tree
    Layer Order Traverse
    Save the queue size before next round of adding left/right children opr
    Then the queue size will be the sublist length
'''

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()
        if not root:
            return []
        else:
            queue.append(root)
        while len(queue) > 0:
            nodeCount = len(queue)
            sublist = []
            for i in range(nodeCount):
                node = queue.popleft()
                sublist.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sublist)

        return ans

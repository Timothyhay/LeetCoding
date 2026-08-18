# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(sub_left, sub_right):
            if not sub_left and not sub_right:
                return True
            if not sub_left or not sub_right:
                return False
            return sub_left.val == sub_right.val and isMirror(sub_left.left, sub_right.right) and isMirror(
                sub_left.right, sub_right.left)

        if not root:
            return True

        return isMirror(root.left, root.right)




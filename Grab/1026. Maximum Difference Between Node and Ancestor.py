'''
    Binart Tree

    Store the intermediate max and min ancestors at the param,
    when encounter leaf return the max-min
    Do the same thing recursively for all the left and right subtrees
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def maxDiff(node, minAnces, maxAnces):
            # if encounter leaves, return the max-min along the path
            if not node:
                return maxAnces - minAnces
            # else, update max and min
            # and return the max of left and right subtrees
            minAnces = min(node.val, minAnces)
            maxAnces = max(node.val, maxAnces)
            left = maxDiff(node.left, minAnces, maxAnces)
            right = maxDiff(node.right, minAnces, maxAnces)

            diff = max(left, right)

            return diff

        return maxDiff(root, root.val, root.val)

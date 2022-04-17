'''
    Binary Tree

    Not every node should compare their value with children's values. So use maxValue and minValue as param!
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        import sys
        
        def checkNode(node, minValue, maxValue):
            if not node:
                return True
            if node.val <= minValue or node.val >= maxValue:
                return False
            
            return checkNode(node.left, minValue, node.val) and checkNode(node.right, node.val, maxValue)
                
        return checkNode(root, -sys.maxsize, sys.maxsize)
        

            
            
        
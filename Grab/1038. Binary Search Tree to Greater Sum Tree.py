'''
    Binary Tree
    Inorder Traverse but in reverse order -> get Largest to Smallest
    Accumulate the intermediate node.val.
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right:
            self.bstToGst(root.right)
        self.pre += root.val
        root.val = self.pre
        if root.left:
            self.bstToGst(root.left)

        return root
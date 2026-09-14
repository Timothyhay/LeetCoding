# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)
        idx = inorder.index(root_val)

        left_in = inorder[:idx]
        right_in = inorder[idx+1:]

        left_post = postorder[:len(left_in)]
        right_post = postorder[len(left_in):-1]

        # return root + preorder(left) + preorder(right)
        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)
        return root

# For list version
'''
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[List]:
    if not inorder:
        return []

    root = postorder[-1]
    idx = inorder.index(root)

    left_in = inorder[:idx]
    right_in = inorder[idx + 1:]

    left_post = postorder[:len(left_in)]
    right_post = postorder[len(left_in):-1]

    # return root + preorder(left) + preorder(right)
    return [root] + self.buildTree(left_in, left_post) + self.buildTree(right_in, right_post)
'''
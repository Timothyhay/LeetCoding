from idlelib.tree import TreeNode
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = float("-inf")

        def sumSubTree(node: Optional[TreeNode]):
            if not node:
                return 0

            left_gain = max(0, sumSubTree(node.left))
            right_gain = max(0, sumSubTree(node.right))
            subtree_gain = node.val + left_gain + right_gain
            self.answer = max(subtree_gain, self.answer)

            # 【关键】返回给上层父节点时，路径不能分叉！
            # - 分叉：把左子树和右子树的贡献（left_gain 和 right_gain）同时加进去；而我们只需要 node.val + node.val + max(left_gain, right_gain)
            # - 不要重复计算：如果用 subtree_gain + max(left_gain, right_gain)，更大的那条分支（max(left_gain, right_gain)）被加了两次。

            # 只能在左子树和右子树中选择更大的一条分支向上延伸
            return node.val + max(left_gain, right_gain)

        sumSubTree(root)
        return self.answer


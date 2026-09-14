# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        # 处理路径从根节点开始的情况
        prefix_sum[0] = 1
        cnt = 0

        def traverse(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val

            cnt = prefix_sum[curr_sum - targetSum]

            # 把当前前缀和加入哈希表
            prefix_sum[curr_sum] += 1

            cnt += traverse(node.left, curr_sum)
            cnt += traverse(node.right, curr_sum)

            # 回溯记得去掉，除非那种每次都新建一个list的题目，不会污染其他调用（右子树）的独立变量
            prefix_sum[curr_sum] -= 1

            return cnt

        return traverse(root, 0)






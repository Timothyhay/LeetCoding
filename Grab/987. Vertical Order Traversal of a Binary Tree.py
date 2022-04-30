'''
    Binary Tree

    Order for col: left to right. For same col, make row order from up to bottom.
    > Use a tuple as hashmap key.
    If two nodes are in the same row and column, the order should be from small to large.
    > Sort it.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        hashtable = dict()

        def traverseLoc(node, row, col):
            if not node:
                return
            if (col, row) in hashtable:
                hashtable[(col, row)].append(node.val)
            else:
                hashtable[(col, row)] = [node.val]
            # print(hashtable[col])
            traverseLoc(node.left, row + 1, col - 1)
            traverseLoc(node.right, row + 1, col + 1)

        traverseLoc(root, 0, 0)
        ans = []
        sublist = []
        cols = list(hashtable.keys())
        cols.sort()
        precol = cols[0][0]
        # print(cols)
        for k in cols:
            if precol != k[0]:
                ans.append(sublist)
                sublist = []
                precol = k[0]
            hashtable[k].sort(reverse=False)
            sublist.extend(hashtable[k])

        if sublist not in ans:
            ans.append(sublist)

        return ans
'''
    Binary Tree
    DFS

    Find the relation between next nodes, connect with node.right/node.next.left.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        def dfs(node, nextnode):
            if not node:
                return
            
            node.next = nextnode
            dfs(node.left, node.right)
            if node.next:
                dfs(node.right, node.next.left)
            else:
                dfs(node.right, None)
            #return node
        
        dfs(root, None)
        return root
            
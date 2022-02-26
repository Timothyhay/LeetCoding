'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for c in s:
            if c != '#':
                s_stack.append(c)
            elif len(s_stack) > 0:
                s_stack.pop()

        for c in t:
            if c != '#':
                t_stack.append(c)
            elif len(t_stack) > 0:
                t_stack.pop()

        return s_stack == t_stack
'''

'''
Time Complexity: O(M + N), where M, N are the lengths of S and T respectively.

Space Complexity: O(M + N).
'''

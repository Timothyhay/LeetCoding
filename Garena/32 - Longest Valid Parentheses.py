

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        cnt = 0
        for c in s:
            if stack[-1] == '(' and c == ')':
                stack.pop()
                cnt += 2
            else:
                stack.append(c)

        return cnt



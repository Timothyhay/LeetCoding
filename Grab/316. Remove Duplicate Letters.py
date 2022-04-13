'''
    String
    Stack

    Pop all the previous elem in the stack not statify the condition: (bigger in lexicographical order and will appear later)

    And all of result char will only appear once. So may maintain a new array to note that - beacuse a real stack has no 'in' function.

'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = dict()
        for i in range(len(s)-1, -1, -1):
            if s[i] not in last_index:
                last_index[s[i]] = i
        
        stack = []
        for i in range(len(s)):
            if s[i] not in stack:
                while len(stack) > 0 and stack[-1] > s[i] and last_index[stack[-1]] > i:
                    stack.pop()
                stack.append(s[i])

        return "".join(stack)
            
        
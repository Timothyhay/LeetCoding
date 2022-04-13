'''
    String
    Simple Stack
'''

lass Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                pair_bracket = pair[c]
                if len(stack) == 0 or stack[-1] != pair_bracket:
                    return False
                else:
                    stack.pop()
            
        if len(stack) == 0:
            return True
                
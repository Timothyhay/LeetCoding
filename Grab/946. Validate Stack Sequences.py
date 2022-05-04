'''
    Stack

    If the stack has say, 2 at the top, then if we have to pop that value next, we must do it now.
    That's because any subsequent push will make the top of the stack different from 2,
    and we will never be able to pop again.
'''


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed and popped:
            return False
        stack = []
        popptr = 0

        for x in pushed:
            stack.append(x)
            while stack and popptr < len(popped) and stack[-1] == popped[popptr]:
                stack.pop()
                popptr += 1

        return popptr == len(popped)
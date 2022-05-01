'''
    Dynamic Programming

    Use a hashmap reachable = defaultdict(set) to save the step can taken from each stone
    e.g.
    [0,1,3,5,6,8,12,17]

    {17={}, 0={1}, 1={1, 2}, 3={1, 2, 3}, 5={1, 2, 3}, 6={1, 2, 3, 4}, 8={1, 2, 3, 4}, 12={3, 4, 5}}
    On each step, we look if any other stone can be reached from it,
    if so, we update that stone's steps by adding step, step + 1, step - 1.
    If we can reach the final stone, we return true.
'''
from collections import defaultdict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Saves the step can taken from this stone
        reachable = defaultdict(set)
        reachable[0] = {1}

        for stone in stones:
            for step in reachable[stone]:

                if step + stone == stones[-1]:
                    return True

                if step + stone in stones:
                    reachable[step + stone].add(step)
                    reachable[step + stone].add(step + 1)
                if step + stone in stones and step - 1 >= 1:
                    reachable[step + stone].add(step - 1)

        return False

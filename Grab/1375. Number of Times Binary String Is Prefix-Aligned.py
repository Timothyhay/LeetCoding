'''
    Array

    if right == i + 1, # i+1 cuz the stepNo. starts from 1; right = right most 1
    it means that all the previous bulbs (to the left) are turned on too.
'''

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        right = -1
        ans = 0
        for step in range(len(flips)):
            right = max(flips[step], right)
            if right == step + 1:
               ans += 1
        
        return ans
            
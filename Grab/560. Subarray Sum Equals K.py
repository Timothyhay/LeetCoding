'''
    Array
    
    Whenever the sums has increased by a value of k, we've found a subarray of sums=k.
    
    If we know SUM[0, i - 1] and SUM[0, j], then we can easily get SUM[i, j]. To achieve this, we just need to go through the array, calculate the current sum and save number of all seen PreSum to a HashMap. 
'''
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        ans = 0
        crtsum = 0
        for num in nums:
            crtsum += num
            # crtsum - X == k  =>  find hashmap[crtsum-k] == X
            ans += hashmap[crtsum-k]
            # Use += 1 to include cases like [-1, 1, 0] (ANS = 3)
            hashmap[crtsum] += 1
        
        return ans
        
        
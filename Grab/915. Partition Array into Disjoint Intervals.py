'''
    Array 

    Use an array to store the min right elem at index i.
'''

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]
        right = [0 for _ in range(len(nums))]
        right[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < right[i+1]:
                right[i] = nums[i]
            else:
                right[i] = right[i+1]
            
            
        for i in range(1, len(nums)):
            right_min = right[i]
            if left_max > right_min:
                left_max = nums[i] if nums[i] > left_max else left_max
            else:
                return i

        return i
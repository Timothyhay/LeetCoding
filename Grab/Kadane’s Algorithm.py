'''
    Kadane’s Algorithm (Dynamic Programming)
    <Maximum Subarray Problem>

    Maximum Subarray Problem
    The maximum subarray problem is the task of finding the largest possible sum of a contiguous subarray,
    within a given one-dimensional array A[1…n] of numbers.

    local_maximum at index i is the maximum of A[i] and the sum of A[i] and local_maximum at index i-1.
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = -10e4
        local_max = 0
        for i in range(len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            if local_max > global_max:
                global_max = local_max

        return global_max
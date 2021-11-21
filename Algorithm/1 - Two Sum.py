class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = dict()

        for i in range(len(nums)):
            t1 = nums[i]
            t2 = target - t1
            # if t1 in pair's keys
            if t1 in pair:
                 return [pair[t1], i]
            else:
                pair[t2] = i

        return -1

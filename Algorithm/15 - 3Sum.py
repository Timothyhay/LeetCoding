class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            # t1 = nums[i]
            # t2 = nums[i+1]
            # t3 = nums[len(nums)-1]
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                lo = i + 1
                hi = len(nums) - 1

                while lo < hi:
                    if nums[lo] + nums[hi] + nums[i] == 0:
                        ans.append([nums[i], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif  nums[lo] + nums[hi] + nums[i] < 0:
                        lo += 1
                    else:
                        hi -= 1

        return ans
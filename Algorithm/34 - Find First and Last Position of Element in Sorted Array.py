from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                upb = mid
                dnb = mid
                while upb < len(nums):
                    if nums[upb] == nums[mid]:
                        upb += 1
                    else:
                        break
                while dnb >= 0:
                    if nums[dnb] == nums[mid]:
                        dnb -= 1
                    else:
                        break
                    
                return [dnb+1, upb-1]
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange(nums = [1], target = 1))

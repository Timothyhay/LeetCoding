from typing import List
# Binary Search
# Do Binary Search twice, or will exceed O(logN) time complexity

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(is_first):
            left = 0
            right = len(nums) - 1
            bound = -1
            while right >= left:
                mid = (right + left) // 2
                if nums[mid] == target:
                    # 如果数组包含大量的重复元素（例如 nums = [8, 8, 8, ..., 8]），线性扩展的过程需要遍历所有 n  个元素。
                    # Linear scan outward from the midpoint results in O(n) worst-case time complexity.
                    # while first > 0 and nums[first-1] == target:
                    #     first -= 1
                    # while last < len(nums)-1 and nums[last+1] == target:
                    #     last += 1
                    bound = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return bound
        return [search(True), search(False)]
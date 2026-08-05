# Binary Search
'''
这道题目的前提是数组为有序数组，同时题目还强调数组中无重复元素，因为一旦有重复元素，使用二分查找法返回的元素下标可能不是唯一的，这些都是使用二分法的前提条件

- while (left <= right) 要使用 <= ，因为left == right是有意义的，所以使用 <=
- if (nums[middle] > target) right 要赋值为 middle - 1，因为当前这个nums[middle]一定不是target，那么接下来要查找的左区间结束下标位置就是 middle - 1

- mid = (right - left) // 2 这个公式算出的是从 0 开始的相对偏移量，而不是从 left 开始的中点索引。正确的公式应该是：
mid = (left + right) // 2

- 如果 target 在数组中不存在，二分查找循环结束时（left > right），left 所代表的位置刚好就是 target 应该插入的位置。
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left



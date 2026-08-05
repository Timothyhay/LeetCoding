# Two Pointers
'''
双指针法（快慢指针法）： 通过一个快指针和慢指针在一个for循环下完成两个for循环的工作。

定义快慢指针
- 快指针：寻找新数组的元素 ，新数组就是不含有目标元素的数组
- 慢指针：指向更新 新数组下标的位置
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        slow_p = 0
        for fast_p in range(len(nums)):
            if nums[fast_p] != 0:
                nums[slow_p] = nums[fast_p]
                slow_p += 1

        for zero_p in range(slow_p, len(nums)):
            nums[zero_p] = 0

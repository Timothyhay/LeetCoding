# Binary Search
'''
二分查找时，时刻记着：
数组是升序（从小到大）排列的 -
- 当前值 < 目标值 → 需要变大 → 左指针向右移 (left = mid + 1)
- 当前值 > 目标值 → 需要变小 → 右指针向左移 (right = mid - 1)

这题只要逻辑上认为二维数组是一个一维数组就可以了。
'''
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while(left <= right):
            mid = (left + right) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                return True
        return False
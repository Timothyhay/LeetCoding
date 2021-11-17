from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if not target in nums:
            return -1
        if len(nums) == 1 and target == nums[0]:
            return 0

        start = 0
        end = len(nums)
        for pivot in range(1, end):
            if nums[pivot] < nums[pivot - 1]:
                break

        crt_end = pivot
        while start <= crt_end:
            mid = start + (crt_end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                crt_end = mid - 1
            else:
                start = mid + 1

        crt_start = pivot
        while crt_start <= end:
            mid = crt_start + (end - crt_start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                crt_start = mid + 1

        return -1
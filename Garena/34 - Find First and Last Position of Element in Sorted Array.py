from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        posFirst = -1
        posLast = -1

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        if nums[start] != target:
            return [-1, -1]
        else:
            posFirst = start

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        posLast = end

        return [posFirst, posLast]





def binSearchOri(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1

# binSearchOri([5,7,7,8,8,10], 8)
# Out[3]: 4
# binSearchOri([5,7,7,8,8,8,8,8,8,10], 8)
# Out[4]: 4
# binSearchOri([5,7,7,8,8,8,8,8,8,8,8,8,8,10], 8)
# Out[5]: 6
# binSearchOri([5,7,7,8,10], 8)
# Out[6]: 3

def binSearchFirst(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] >= target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
    if nums[start] != target:
        return -1
    else:
        return start

# binSearchFirst([5,7,7,8,10], 8)
# Out[8]: 3
# binSearchFirst([5,7,7,8,8,8,8,8,8,8,8,8,8,10], 8)
# Out[9]: 3
# binSearchFirst([5,7,7,8,8,8,8,8,8,10], 8)
# Out[10]: 3
# binSearchFirst([5,7,7,8,8,10], 8)
# Out[11]: 3

def binSearchLast(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    if nums[end] != target:
        return -1
    else:
        return end

# binSearchLast([5,7,7,8,8,8,8,8,8,10], 8)
# Out[19]: 8
# binSearchLast([5,7,7,8,8,10], 8)
# Out[20]: 4
# binSearchLast([5,7,7,8,8,8,8,8,10], 8)
# Out[21]: 7
# binSearchLast([5,7,7,8,8,8,8,10], 8)
# Out[22]: 6
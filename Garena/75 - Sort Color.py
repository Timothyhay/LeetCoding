'''
https://en.wikipedia.org/wiki/Dutch_national_flag_problem
Pseudocode
The following pseudocode for three-way partitioning which assumes zero-based array indexing was proposed by Dijkstra himself.[2] It uses three indices i, j and k, maintaining the invariant that i ≤ j ≤ k.

Entries from 0 up to (but not including) i are values less than mid,
entries from i up to (but not including) j are values equal to mid,
entries from j up to (and including) k are values not yet sorted, and
entries from k + 1 to the end of the array are values greater than mid.

procedure three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    k ← size of A - 1

    while j <= k:
        if A[j] < mid:
            swap A[i] and A[j]
            i ← i + 1
            j ← j + 1
        else if A[j] > mid:
            swap A[j] and A[k]
            k ← k - 1
        else:
            j ← j + 1
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = len(nums) - 1
        while white <= blue:
            if nums[white] < 1:
                temp = nums[red]
                nums[red] = nums[white]
                nums[white] = temp
                red += 1
                white += 1
            elif nums[white] > 1:
                temp = nums[blue]
                nums[blue] = nums[white]
                nums[white] = temp
                blue -= 1
            else:
                white += 1


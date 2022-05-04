'''
    Binary Search

    Assume A[mid] ~ A[mid + k] is sliding window

    case 1: x - A[mid] < A[mid + k] - x, need to move window go left
    -------x----A[mid]-----------------A[mid + k]----------

    case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
    -------A[mid]----x-----------------A[mid + k]----------

    case 3: x - A[mid] > A[mid + k] - x, need to move window go right
    -------A[mid]------------------x---A[mid + k]----------

    [case 4: x - A[mid] > A[mid + k] - x, need to move window go right]
    -------A[mid]---------------------A[mid + k]----x------

    If x - A[mid] > A[mid + k] - x,
    it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
    and we have mid smaller than the right i.
    So assign left = mid + 1.
'''

class Solution:

    def findClosestElements(self, A, k, x):
            left, right = 0, len(A) - k
            while left < right:
                mid = (left + right) // 2
                if x - A[mid] > A[mid + k] - x:
                    left = mid + 1
                else:
                    right = mid
            return A[left:left + k]
def solution(A):
    dist = set(A)
    return len(dist)

# Or with sorting:
'''
O(n log n): First, sort array A; similar values will then be next to each other.
Finally, just count the number of distinct pairs in adjacent cells.

def distinct(A):
    n = len(A)
    A.sort()
    result = 1
    for k in xrange(1, n):
        if A[k] != A[k - 1]:
        result += 1
    return result
'''


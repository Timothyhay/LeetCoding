
def solution(A):
    sumA = 0
    for a in A:
        sumA += a

    # Note: Always set the default min value to INF instead of a possible value!
    # Cuz sum(A) may not be the largest one
    minD = float('inf')
    left = 0
    right = sumA
    for i in range(0, len(A) - 1):
        left += A[i]
        right -= A[i]
        # print(abs(right - left), minD)
        minD = min(abs(right - left), minD)

    return minD

solution([ -1000, 1000, -500, 990])
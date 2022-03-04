def solution(A):
    if not A:
        return 1

    A.sort()
    for i in range(1, len(A) + 1):
        if A[i - 1] != i:
            return i

    return len(A) + 1


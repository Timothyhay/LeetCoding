def solution(X, A):
    leavesNeed = X
    leaves = [0] * (X + 1)
    for i, pos in enumerate(A):
        if not leaves[pos]:
            leaves[pos] += 1
            leavesNeed -= 1
        if leavesNeed == 0:
            return i
    return -1


# O(n^2)
'''
def solution(A):
    passCnt = 0

    for i, elem in enumerate(A):
        for j in range(i + 1, len(A)):
            if elem == 0 and A[j] == 1:
                passCnt += 1
            if passCnt > 1000000000:
                return -1

    return passCnt
'''

#  O(n)
def solution(A):
    passCnt = 0
    east = 0
    for car in A:
        if car == 0:
            # Use this ease var till the end
            east += 1
        else:
            passCnt += east
            if passCnt > 1e9:
                return -1
    return passCnt
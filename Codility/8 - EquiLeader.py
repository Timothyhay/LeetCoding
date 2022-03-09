

# Notice that the sequence can have at most one leader.

# Notice that if the sequence a0, a1, . . . , an−1 contains a leader, then after removing a pair of
# elements of different values, the remaining sequence still has the same leader.
# Indeed, if we remove two different elements then only one of them could be the leader


def solution(A):
    if not A:
        return 0

    backup = A.copy()
    backup.sort()
    candidate = backup[len(A) // 2]
    cnt = 0
    for elem in backup:
        if elem == candidate:
            cnt += 1
    if cnt <= len(A) // 2:
        return 0

    leftcnt = 0
    ans = 0
    for i in range(len(A) - 1):
        # The leader in left and right side should be the same!
        if A[i] == candidate:
            leftcnt += 1
        if leftcnt > (i + 1) // 2:
            rightcnt = cnt - leftcnt
            if rightcnt > (len(A) - i - 1) // 2:
                ans += 1

    return ans


'''

single
single element✔OK
▶double

'''
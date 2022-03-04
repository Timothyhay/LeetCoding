from collections import defaultdict

def solution(A):
    # Do not use (max+1) cuz may encounter elements with minimal/maximal value -> MemoryError
    # Use defaultdict to avoid unnecessary 0s
    perm = defaultdict(int)
    cnt = max(A)
    for a in A:
        perm[a] += 1
        if perm[a] == 1:
            cnt -= 1
        elif perm[a] > 1:
            return 0
    if cnt != 0:
        return 0
    else:
        return 1

'''
def solution(A):
    # Do not use (max+1) cuz may encounter elements with minimal/maximal value -> MemoryError
    perm = [0] * max(A)
    cnt = max(A)
    for a in A:
        perm[a] += 1
        if perm[a] == 1:
            cnt -= 1
        elif perm[a] > 1:
            return 0
    if cnt != 0:
        return 0
    else:
        return 1
        
extreme_min_max
single element with minimal/maximal value✘RUNTIME ERROR
tested program terminated with exit code 1

  File "/tmp/solution.py", line 2, in solution
    perm = [0] * (max(A) + 1)
MemoryError
'''
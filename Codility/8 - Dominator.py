
def solution(A):
    if not A:
        return -1
    backup = A.copy()
    A.sort()
    cancidate = A[len(A) // 2]
    cnt = 0
    for a in A:
        if a == cancidate:
            cnt += 1
    if cnt <= len(A) // 2:
        return -1

    for i, a in enumerate(backup):
        if a == cancidate:
            return i


'''
small_half_positions
half elements the same, and half + 1 elements the same✘WRONG ANSWER

got 10, but element is not a dominator, value 2 has only 10 occurences (n=20)


extreme_empty_and_single_item
empty and single element arrays✘RUNTIME ERROR

tested program terminated with exit code 1
'''
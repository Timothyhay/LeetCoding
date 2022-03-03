def solution(A):
    hashset = set()
    for i in A:
        if i not in hashset:
            hashset.add(i)
        else:
            hashset.discard(i)

    return list(hashset)[0]

solution([9, 3, 9, 3, 9, 7, 9])
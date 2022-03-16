def solution(A):
    if len(A) < 3:
        return 0
    
    A.sort()
    for i in range(len(A)-2):
        a = A[i]
        b = A[i+1]
        c = A[i+2]
        if a + b > c and a + c > b and b + c > a:
            return 1
    
    return 0
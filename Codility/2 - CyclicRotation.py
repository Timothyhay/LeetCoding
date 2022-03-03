def solution(A, K):
    if not A:
        return []

    K = K % len(A)
    ans = [-1] * len(A)

    for i in range(len(A) - K):
        ans[i + K] = A[i]
    for i in range(len(A) - K, len(A)):
        ans[i - len(A) + K] = A[i]

    return ans

solution([0, 0, 0], 1)

'''
Correctness tests

▶extreme_empty
empty array✘RUNTIME ERROR
tested program terminated with exit code 1

▶single
one element, 0 <= K <= 5✔OK
▶double
two elements, K <= N✔OK
▶small1
small functional tests, K < N✔OK
▶small2
small functional tests, K >= N✔OK
▶small_random_all_rotations
small random sequence, all rotations, N = 15✔OK
▶medium_random
medium random sequence, N = 100✔OK
▶maximal
'''
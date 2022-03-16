
def solution(A):
    A.sort()
    candidate = A[-1] * A[-2] * A[-3]
    if A[0] >= 0:
        return candidate
    else:
        candidate_neg = A[-1] * A[0] * A[1]
        return candidate if candidate > candidate_neg else candidate_neg 



'''
Note: neg * neg can also get pos number.

The following issues have been detected: wrong answers.
For example, for the input [-5, 5, -5, 4] the solution returned a wrong answer (got -100 expected 125).
'''
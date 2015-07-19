# Name: Distinct
# Link: https://codility.com/demo/take-sample-test/distinct/


def solution(A):
    N = len(A)
    result = 1

    A.sort()
     
    # No elements than result is 0
    if N == 0:
        return 0

    # Itetates through A, and for each new value adds one to the result
    for k in xrange(1, N):
        if A[k - 1] != A[k]:
            result += 1
        
    return result

# Name: Triangle
# Link: https://codility.com/demo/take-sample-test/triangle/


def solution(A):
    N = len(A)
    A.sort()
    
    # If A length is lesser than 3 A can't be triangular
    if N < 3:
        return 0

    # Since Array is sorted, only have to look for each element once
    for k in xrange(N - 1):
        if test_triangle(A[k], A[k + 1], A[k + 2]):
            return 1    

    return 0

def test_triangle(P, Q, R):
    return (P + Q) > R and (Q + R) > P and (R + P) > Q

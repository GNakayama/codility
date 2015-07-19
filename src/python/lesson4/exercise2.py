# Name: Triangle
# Link: https://codility.com/demo/take-sample-test/triangle/


def solution(A):
    N = len(A)
    A.sort()
    
    # If A length is 3 this the only combination to check
    if N == 3 and test_triangle(A[0], A[1], A[2]):
        return 1

    # Since Array is sorted, only have to look for each element once
    for k in xrange(N - 1):
        if test_triangle(A[k], A[k + 1], A[k + 2]):
            return 1    

    return 0

def test_triangle(P, Q, R):
    return (P + Q) > R and (Q + R) > P and (R + P) > Q

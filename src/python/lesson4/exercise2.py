def solution(A):
    N = len(A)
    A.sort()
    
    if N > 3:        
        for k in xrange(N - 2):       
        
            if test_triangle(A[k], A[k + 1], A[k + 2]):
                return 1
    else:
        if N == 3:
            if test_triangle(A[0], A[1], A[2]):
                return 1
    
    return 0


def test_triangle(P, Q, R):
    return (P + Q) > R and (Q + R) > P and (R + P) > Q

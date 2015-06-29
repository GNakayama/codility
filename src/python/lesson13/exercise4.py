def solution(A):
    N = len(A)
    result = 0
    A.sort()
    
    for P in xrange(N):
        R = 0
        for Q in xrange(P + 1, N):
            while R < N and (A[P] + A[Q]) > A[R]:            
                R += 1 
                
            result += R - Q - 1
    
    return result
    

def is_triangle(P, Q, R):
    return (P + Q) > R and (P + R) > Q and (R + Q) > P

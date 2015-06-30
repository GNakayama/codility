def solution(K, A):
    N = len(A)
    result = 0
    length = 0
    
    for k in xrange(N):
        length += A[k]
        
        if length >= K:
            result += 1
            length = 0
    
    return result

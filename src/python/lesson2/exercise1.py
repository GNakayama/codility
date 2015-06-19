def solution(X, A):
    n = len(A)
    count = [0] * (X + 1)
    total = 0
        
    for k in xrange(n):        
        if count[A[k]] == 0:
            total += 1
            
            if total == X:
                return k
        
        count[A[k]] = 1
        
    
    return -1

def solution(A):
    n = len(A)
    count = [0]*(n + 1)
    max = True
        
    for k in xrange(n):
        if  (n + 1) > A[k] > 0:
            count[A[k]] += 1
    
    
    for k in xrange(1, n + 1):
        if count[k] == 0:
            return k
    
    return n + 1

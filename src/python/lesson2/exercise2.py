def solution(A):
    n = len(A)
    total = 0
    count = [0]*(n + 1)
        
    for k in xrange(n):
        if A[k] > n:
            return 0;
        if count[A[k]] == 0:
            total += 1
            count[A[k]] += 1
        else:
            return 0    
    
    if total == n:
        return 1
    
    return 0

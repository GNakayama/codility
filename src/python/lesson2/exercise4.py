def solution(N, A):
    m = len(A)
    count = [0]*(N + 1)
    maxi = 0
    offset = 0
    
    for k in xrange(m):
        if A[k] > N:
            offset = maxi
        else:
            count[A[k]] = max(offset + 1, count[A[k]] + 1)
            
            if maxi < count[A[k]]:
                maxi = count[A[k]]
    
    for k in xrange(1, N + 1):
        if count[k] < offset:
            count[k] = offset
        
    return count[1:]

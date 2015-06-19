def solution(A):
    return goldenLeader(A)


def goldenLeader(A):
    n = len(A)
    size = 0
    index = -1
    
    for k in xrange(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    
    if (size > 0):
        candidate = value
        count = 0
        
        for k in xrange(n):
            if (A[k] == candidate):
                count += 1            
                
                if (count > n // 2):
                    return k
    
    return -1

def solution(A):    
    total = sum(A)
    r = -1
    a = 0
    
    for p in range(1, len(A)):
        a += A[p - 1]
        b = abs(2*a - total)
                
        if b < r or r == -1:
            r = b
    
    return r

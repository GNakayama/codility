def solution(N):
    result = 2*(1 + N)
    
    k = 2
    while k*k <= N:
        if N%k == 0:
            result = min(result, 2*(k + N/k))
        
        k += 1
    return result

def solution(A):
    A.sort()
    N = len(A)
    result = 1
    i = 1
    
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    
    while i < (N - 1):
        if A[i - 1] != A[i]:
            result += 1
            i += 1
        else:
            while i < N and A[i - 1] == A[i]:
                i += 1
        
    if A[N - 1] != A[N - 2]:
        result += 1
        
    return result

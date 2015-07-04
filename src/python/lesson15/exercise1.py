def solution(A):
    N = len(A)
    
    if N < 2:
        return A[0] + A[1]
    
    result = [0] * 7
        
    for dice in xrange(7):       
        if dice == 0:
            result[dice] = A[0]
        elif dice < N:
            result[dice] = A[0] + A[dice]
    
    for k in xrange(1, N):
        for dice in xrange(7):
            if dice == 0:
                result[dice] = result[1]
            elif dice == 6 and k + dice < N:
                result[dice] = result[0] + A[k + dice] 
            elif k + dice < N:
                result[dice] = max(result[dice + 1], result[0] + A[k + dice])
            else:
                break
                    
    return result[0]

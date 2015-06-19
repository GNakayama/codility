def solution(S):
    N = len(S)
    size = 0
    
    for k in xrange(N):
        if S[k] == '(':
            size += 1
        else:
            size -= 1
        
        if size < 0:
            return 0
    
    
    if size == 0:
        return 1
    else:
        return 0

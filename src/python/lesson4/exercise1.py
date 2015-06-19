def solution(A):
    N = len(A)
    maxs = [None]*3
    mins = [1000]*2
    
    if N == 3:
        return A[0]*A[1]*A[2]
    
    for k in xrange(N):
        if maxs[0] == None or A[k] > maxs[0]:
            if mins[0] == None or maxs[2] < mins[0]:
                mins[1] = mins[0]
                mins[0] = maxs[2]
            elif  mins[1] == None or maxs[2] < mins[1]:
                mins[1] = maxs[2]
            
            maxs[2] = maxs[1]
            maxs[1] = maxs[0]
            maxs[0] = A[k]
        elif maxs[1] == None or A[k] > maxs[1]:
            if mins[0] == None or maxs[2] < mins[0]:
                mins[1] = mins[0]
                mins[0] = maxs[2]
            elif  mins[1] == None or maxs[2] < mins[1]:
                mins[1] = maxs[2]
                
            maxs[2] = maxs[1]
            maxs[1] = A[k]
        elif maxs[2] == None or A[k] > maxs[2]:            
            if mins[0] == None or maxs[2] < mins[0]:
                mins[1] = mins[0]
                mins[0] = maxs[2]
            elif  mins[1] == None or maxs[2] < mins[1]:
                mins[1] = maxs[2]
            
            maxs[2] = A[k]
        elif mins[0] == None or A[k] < mins[0]:
            mins[1] = mins[0]
            mins[0] = A[k]
        elif mins[1] == None or A[k] < mins[1]:
            mins[1] = A[k]
    
    if mins[1] == None:
        return max(maxs[0]*maxs[1]*maxs[2], maxs[0]*maxs[2]*mins[0])
    
    return max(maxs[0]*maxs[1]*maxs[2], maxs[0]*mins[0]*mins[1])

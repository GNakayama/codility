def solution(A):
    N = len(A)
    max_slice = 0 
    max_ending = 200001
    
    for k in xrange(N):
        max_slice = max(max_slice, A[k] - max_ending)
    
        if max_ending > A[k]:
            max_ending = A[k]      
    
    return max_slice

def solution(A):
    return golden_max_slice(A)


def golden_max_slice(A):
    N = len(A)
    max_ending = max_slice = A[0]

    
    for k in xrange(1, N):
        if max_slice < 0:
            if max_slice < A[k]:
                max_slice = A[k]
                max_ending = A[k]
        else:        
            max_ending = max(0, max_ending + A[k])
            max_slice = max(max_slice, max_ending)
    
    return max_slice

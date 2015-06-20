def solution(A):
    N = len(A)
    smaller = 10001
        
    if N == 3:
        return 0
    
    max_slice, begin, end = golden_max_slice(A)
    
    if begin == 0 and end == N - 1:
        max_slice, begin, end = golden_max_slice(A[(begin + 1):end])
        begin += 1
        end += 1
    elif begin == 0:
        max_slice, begin, end = golden_max_slice(A[(begin + 1):])
        begin += 1
        end += 1
    elif end == N - 1:
        max_slice, begin, end = golden_max_slice(A[:end])
    
    for k in xrange(begin, end + 1):
        if smaller > A[k]:
            smaller = A[k]
            smaller_index = k
        
    max_right = 0
    max_left = 0
    parcel_sum = 0
    
    for k in xrange(end + 2, N - 1):
        parcel_sum += A[k]
        max_right = max(max_right, parcel_sum)
    
    parcel_sum = 0
        
    for k in xrange(begin - 2, 0, -1):
        parcel_sum += A[k]
        max_left = max(max_left, parcel_sum)
    
    if max_right > abs(smaller) or max_left > abs(smaller):
        if max_right == 0:
            max_slice += max_left
        elif max_left == 0:
            max_slice += max_right
        elif max_right > max_left:
            max_slice += max_right
        else:
            max_slice += max_left    
    else:
        if smaller < 0 or (begin == 1 and end == (N - 2)):
            max_slice -= A[smaller_index]        
    
    return max(0, max_slice)   

def golden_max_slice(A):
    N = len(A)
    max_ending = max_slice = A[0]
    i = 0
    i_aux = 0
    j = 0

    for k in xrange(1, N):
        if max_slice < 0:
            if max_slice < A[k]:
                max_slice = A[k]
                max_ending = A[k]
                i = k
                i_aux = k
                j = k
        else:      
            if max_ending == 0 and A[k] > 0:
                i_aux = k
            
            max_ending = max(0, max_ending + A[k])
                                    
            if max_slice < max_ending:
                if i != i_aux:
                    i = i_aux
                j = k
                        
            max_slice = max(max_slice, max_ending)
    
    return max_slice, i, j

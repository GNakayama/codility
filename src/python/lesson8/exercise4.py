def solution(A):
    N = len(A)
    peaks = find_peaks(A)
    n_peaks = len(peaks)
    max_flags = n_peaks
    again = True
        
    while N < max_flags*(max_flags - 1) + 3 and max_flags > 0:
        max_flags -= 1
        
    while again:
        again = False
        i = 0
        max_aux = max_flags - 1
        
        for k in xrange(1, n_peaks):
            if peaks[k] - peaks[i] >= max_flags:
                i = k
                max_aux -= 1
                
                if max_aux == 0:
                    return max_flags
            
            if (n_peaks - (k + 1)) < max_aux:
                again = True
                max_flags -= 1    
                break
        
    return max_flags


def find_peaks(A):
    N = len(A)
    peaks = []

    for k in xrange(1, N - 1):
        if A[k - 1] < A[k] > A[k + 1]:
            peaks.append(k)

    return peaks

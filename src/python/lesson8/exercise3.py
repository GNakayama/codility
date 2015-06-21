def solution(A):
    N = len(A)
    peaks = find_peaks(A)
    n_peaks = len(peaks)
    result = n_peaks    
    again = True
        
    while again and result > 0:
        again = False
    
        while not N%result == 0:
            result -= 1
        
        i = 0
        size = N/result
        
        for k in xrange(n_peaks):
            if size*(i) <= peaks[k] < size*(i +1):
                if (i + 1) == result:
                    break
                
                i += 1
            
            if (result - i) > (n_peaks - (k + 1)):                
                again = True
                result -= 1
                break
            
    return result
    
def find_peaks(A):
    N = len(A)
    peaks = []
    
    for k in xrange(1, N - 1):
        if A[k - 1] < A[k] > A[k + 1]:
            peaks.append(k)
    
    return peaks

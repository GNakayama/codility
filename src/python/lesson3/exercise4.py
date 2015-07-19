# Name: MinAvgTwoSlice
# Link: https://codility.com/demo/take-sample-test/min_avg_two_slice/


def solution(A):
    N = len(A)
    result = 0
    
    # If N  == 2 the only possible result is 0
    if N == 2:
        return 0
    
    # calc prefix sum
    pref = prefix_sum(A)
    
    start = 0
    min_average =  float(pref[2] - pref[result])/2
    
    for k in xrange(2, N):
        average = float(pref[k + 1] - pref[start])/(k - start + 1)        

        if average < float(pref[k] - pref[start])/(k - start):
            start = k - 1
            
            if float(pref[k + 1] - pref[start - 1])/(k - start + 2) <= float(pref[k + 1] - pref[start])/(k - start + 1):
                start -= 1
            
            average = float(pref[k + 1] - pref[start])/(k - start + 1)  
                                 
        if average < min_average:
            result = start
            min_average = average
        
        k += 1
        
    return result


# Prefix Sum
def prefix_sum(A):
    N = len(A)
    result = [0]*(N + 1)
    
    for k in xrange(1, N + 1):
        result[k] = result[k - 1] + A[k - 1] 
        
    return result

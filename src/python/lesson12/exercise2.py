def solution(A, B, C):
    result = -1
    lowerBound = 1
    upperBound = len(C)
        
    while lowerBound <= upperBound:
        middle = (lowerBound + upperBound)/2
        
        if nailed(A, B, C, middle):
            upperBound = middle - 1
            result = middle
        else:
            lowerBound = middle + 1
            
    return result

def count_nails(C, M):
    count = [0]*(2*M + 1)
    
    for k in xrange(len(C)):
        count[C[k]] = 1
    
    return count
    
def prefix_sum(A):
    N = len(A)
    pref = [0]*(N + 1)
        
    for k in xrange(1, N + 1):
        pref[k] = pref[k - 1] + A[k - 1]
    
    return pref

def nailed(A, B, C, middle):
    N = len(A)    
    nails_count = count_nails(C[:middle], len(C))
    pref_nails = prefix_sum(nails_count)
    
    for k in xrange(N):
        nailed = False
        
        if not pref_nails[B[k] + 1] - pref_nails[A[k]] > 0:
            return False
    
    return True

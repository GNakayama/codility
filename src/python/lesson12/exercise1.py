def solution(K, M, A):
    lowerBound = max(A)
    upperBound = sum(A)
    result = lowerBound
 
    if K == 1:      
        return upperBound
    
    if K >= len(A): 
        return lowerBound
 
    while lowerBound <= upperBound:
        middle = (lowerBound + upperBound) / 2       
        blocks = count_blocks(A, middle)
        
        if blocks <= K:
            upperBound = middle - 1
            result = middle
        else:
            lowerBound = middle + 1
 
    return result

def count_blocks(A, max_element):
    result = 1   
    N =  len(A)
    total = 0
    
    for k in xrange(N):
        total += A[k]
        
        if total > max_element:
            result += 1            
            total = A[k]
            
    return result

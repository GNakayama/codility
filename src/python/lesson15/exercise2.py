def solution(A):
    N  = len(A)
    total = 0
    max_element = 0
    
    if N == 0:
        return 0
    
    if N == 1:
        return A[0]
    
    max_element = A[0]
    
    for k in xrange(N):
        A[k] = abs(A[k])
        total += A[k]
        max_element = max(abs(A[k]), max_element)
    
    final = total
    count = [0]*(max_element + 1)
    result = [0]*(max_element + 1)
        
    for k in xrange(N):
        count[A[k]] += 1
    
    if A[0] >= total//2:
        return abs((total - 2*A[0]))

    result[A[0]] += A[0]
    count[A[0]] -= 1
    for i in xrange(max_element + 1):
        if count[i] > 0 and not i == A[0]:
            if result[A[0]] + i <= total//2: 
                result[i] = result[A[0]] + i
                final = min(final, abs(total - 2*result[i]))
        
    if count[A[0]] > 0:
        if result[A[0]] + A[0] <= total//2: 
            result[A[0]] = result[A[0]] + A[0]
            final = min(final, abs(total - 2*result[i]))
    
    for k in xrange(1, N):
        if A[k] >= total//2:
            return abs((total - 2*A[k]))
        
        count[A[k]] -= 1
               
        for i in xrange(max_element + 1):
            if count[i] > 0 and not i == A[k]:
                if result[A[k]] + i <= total//2: 
                    result[i] = result[A[k]] + i
                    final = min(final, abs(total - 2*result[i]))
                else:
                    result[i] = max(result[A[k]], result[i])
                    final = min(final, abs(total - 2*(result[A[k]] + i)))               
            
        if count[A[k]] > 0:
            if result[A[k]] + A[k] <= total//2: 
                result[A[k]] = result[A[k]] + A[k]
            
            final = min(final, abs(total - 2*result[A[k]]))

    return final
    
    
    

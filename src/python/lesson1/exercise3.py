def solution(A):
    n = len(A)    
    total = ((n + 1)*(n + 2))/2
    
    for i in range(n):
        total -= A[i]
    
    return total

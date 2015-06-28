def solution(A):
    N = len(A)
    max_element =  min(abs(A[0]), abs(A[-1]))
    result = 1
    front = 1
    
    for k in xrange(1,N): 
        if abs(A[k]) < max_element:
            if A[k] <= 0 and not A[k] == A[k - 1]:
                result += 1
        
            front += 1
    
    front -= 1
    
    for back in xrange(N):        
        if abs(A[back]) > max_element:
            if back == N - 1 or not A[back] == A[back + 1]:
                result += 1
        elif front > back:
            while front >= 0 and A[front] > abs(A[back]):
                if front == 0 or not A[front] == A[front - 1]:
                    result += 1
                
                front -= 1
            
            while front >= 0 and A[front] == abs(A[back]):
                front -= 1
        
    return result

def solution(A):
    N = len(A)
    A.sort()
    front = 0
    back = len(A) - 1
    result =  abs(A[back] + A[front])
    
    while back >= front:
        addition = A[back] + A[front]
        
        if addition < 0:
            result = min(result, abs(addition))
            front += 1
        elif addition == 0:
            return 0
        else:
            result = min(result, abs(addition))
            back -= 1
    
    return result

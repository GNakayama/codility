def solution(A):
    return golden_max_slice(A)
    
def golden_max_slice(A):
    max_ending = 0 
    max_slice = 0
    
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    
    return max_slice

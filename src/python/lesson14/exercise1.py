#Name: MaxNonoverlappingSegments
#Link: https://codility.com/demo/take-sample-test/max_nonoverlapping_segments/

def solution(A, B):
    result = 0
    N = len(A)
    
    if N == 0:
        return 0
    
    result += 1
    segment = 0 
    
    for k in xrange(1, N):
        if B[k] > B[segment] < A[k]:
            result += 1
            segment = k
    
    return result

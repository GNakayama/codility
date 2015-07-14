# Name: MissingInteger
# Link: https://codility.com/demo/take-sample-test/missing_integer/


def solution(A):
    N = len(A)
    count = [0]*(N + 1)
    
    # Counts all elements of A tha belongs to sequence {1, ..., N}
    for k in xrange(N):
	if N >= A[k] > 0:
            count[A[k]] += 1
    
    # Searches for the lesser integer that not belongs to A 
    for k in xrange(1, N + 1):
        if count[k] == 0:
            return k
    
    # If A has all elements from 1 to N, N + 1 is the minimal integer
    return N + 1

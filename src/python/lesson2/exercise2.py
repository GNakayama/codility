# Name: PermCheck
# Link: https://codility.com/demo/take-sample-test/perm_check/


def solution(A):
    N = len(A)
    # Counts appearance of elements of the sequence {1...N}
    count = [0]*(N + 1)
        
    for k in xrange(N):
        # If A has an element greater than N, A can't be a permutation from 1 to N
        if A[k] > N:
            return 0;
        # If it's the first time that A[k] appears count that, otherwise A can't be a permutation from 1 to N
        if count[A[k]] == 0:
            count[A[k]] = 1
        else:
            return 0    
    
    return 1

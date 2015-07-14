# Name: MaxCounters 
# Link: https://codility.com/demo/take-sample-test/max_counters/


def solution(N, A):
    M = len(A)
    count = [0]*(N + 1)
    max_counter = 0
    offset = 0
    
    for k in xrange(M):
        # max counter operation, defines a offset with the value of the max counter of the count array at the time 
        if A[k] > N:
            offset = max_counter
        # increase(x) operation, id a max counter operation happened updates the count of the element A[k] accordingly
        else:
            count[A[k]] = max(offset + 1, count[A[k]] + 1)

            # Tracks the max counter value of the count array 
            if max_counter < count[A[k]]:
                max_counter = count[A[k]]
    
    # Updates the values that were not updated before by the max counter operation
    for k in xrange(1, N + 1):
        if count[k] < offset:
            count[k] = offset
        
    return count[1:]

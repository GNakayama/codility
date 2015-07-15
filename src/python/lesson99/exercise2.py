# Name: OddOccurrencesInArray
# Link: https://codility.com/demo/take-sample-test/odd_occurrences_in_array/


def solution(A):
    N = len(A)
    result = A[0]
    
    for k in xrange(1, N):
        result ^= A[k]
    
    return result

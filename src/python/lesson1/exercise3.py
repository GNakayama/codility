# Name: PermMissingElem
# Link: https://codility.com/demo/take-sample-test/perm_missing_elem/


def solution(A):
    N = len(A)    
    # Calcs the sum of all integers from 1 to N + 1
    total = ((N + 1)*(N + 2))/2
    
    for i in range(N):
        # Removes all the elements of the array, from the sum, in the end this will gives us the missing element.
        total -= A[i]
    
    return total

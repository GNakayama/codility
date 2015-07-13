# Name FrogRiverOne
# Link https://codility.com/demo/take-sample-test/frog_river_one/


def solution(X, A):
    N = len(A)
    # Counts the appearance of leaves at every position from the 1 to X
    count = [0] * (X + 1)
    total = 0
        
    for k in xrange(N):        
        # If it's the first time that the leaf appears at position A[k] adds one to total
        if count[A[k]] == 0:
            total += 1

            # If there is a leaf in every position from 1 to X, returns the current array index
            if total == X:
                return k
        # Marks the position A[k] with a leaf
        count[A[k]] = 1       
    
    return -1

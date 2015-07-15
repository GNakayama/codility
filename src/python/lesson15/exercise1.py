
# Name: NumbertSolitarie
# Link: https://codility.com/demo/take-sample-test/number_solitaire/


def solution(A):
    N = len(A)
    
    # If we have only two elements the result should be the sum of this elements
    if N < 2:
        return A[0] + A[1]
    
    result = [0] * 7
    result[0] = A[0]
    # First iteration, sets the first values for the result array
    for dice in xrange(7):       
        # The first movement so A[0] plus the next house ranging from 1 to 6, 
        # notice that, if we have less than 6 houses on our board we have to ignore the results
        if dice < N:
            result[dice] = A[0] + A[dice]
    
    # Greedy loop
    for k in xrange(1, N):
	# First set the maximum result that got us at index k
        result[0] = result[1]
	# Calcs the next five (from 1 to 5) possible results departing from index k
        for dice in xrange(1, 6):
            if k + dice < N:
  		# Keeps the greater result, to reach the house k + dice, 
                # going trough house k may decrease the result, so we ignore it if that's it the case
                result[dice] = max(result[dice + 1], result[0] + A[k + dice])
            else:
		# We made all the necessary calculations
                break
         
        # It's the first time we reached this house, so no need to do max() here          
        if k + 6 < N:
            result[6] = result[0] + A[k + 6]
 
    return result[0]

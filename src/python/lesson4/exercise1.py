# Name: MaxProductOhThree
# Link: https://codility.com/demo/take-sample-test/max_product_of_three/


def solution(A):
    N = len(A)
    maxs = [0]*3
    mins = [1001]*2
   
    if N == 3:
        return A[0]*A[1]*A[2]
    
    maxs[0] = max([A[0], A[1], A[2]])
    
    # Prepares the maxs array
    if maxs[0] == A[0]:
        maxs[1] = max([A[1], A[2]])
        
        if maxs[1] == A[1]:
            maxs[2] = A[2]
        else:
            maxs[2] = A[1]           
    elif maxs[0] == A[1]:
        maxs[1] = max([A[0], A[2]])
        
        if maxs[1] == A[0]:
            maxs[2] = A[2]
        else:
            maxs[2] = A[0]
    else:
        maxs[1] = max([A[0], A[1]])
        
        if maxs[1] == A[0]:
            maxs[2] = A[1]
        else:
            maxs[2] = A[0]
    
    # Iterate to find the three maxs and two mins if it exists 
    # Shift maxs if A[k] is greter than any element of maxs
    # maxs[2] could be a min.
    for k in xrange(3, N):
        if A[k] > maxs[0]:
            switch(mins, maxs[2])

            maxs[2] = maxs[1]
            maxs[1] = maxs[0]
            maxs[0] = A[k]
        elif A[k] > maxs[1]:
            switch(mins, maxs[2])

            maxs[2] = maxs[1]
            maxs[1] = A[k]
        elif A[k] > maxs[2]:
            switch(mins, maxs[2])

            maxs[2] = A[k]
        else:
            switch(mins, A[k])

    # If has only one minimum
    if mins[1] == 1001:
	# if maxs[2] < 0, mins[0]*maxs[2] > 0, and could be greater than maxs[1]*maxs[2]
        return max(maxs[0]*maxs[1]*maxs[2], maxs[0]*maxs[2]*mins[0])

    # If mins < 0, mins[0]*mins[1] > 0 and could be greater than maxs[1]*maxs[2]
    return max(maxs[0]*maxs[1]*maxs[2], maxs[0]*mins[0]*mins[1])


# Shift mins if n is lesser than any elements of mins
def switch(mins, n):
    if n < mins[0]:
        mins[1] = mins[0]
        mins[0] = n
    elif n < mins[1]:
        mins[1] = n

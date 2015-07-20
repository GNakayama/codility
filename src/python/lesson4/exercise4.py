# Name: NumberOfDiscIntersections
# Link: https://codility.com/demo/take-sample-test/number_of_disc_intersections/


def solution(A):
    N = len(A)
    result = 0  
    min_intersect = [0]*N
    max_intersect = [0]*N
        
    for k in xrange(N):
        #Counts how many circles intersect point max_reach, at the right side of the circle
        #e.g. max_reach = position in X + radius
        #If max_reach is greater than N - 1, we would say that the circle intersects at N - 1
        max_intersect[min(N - 1, k + A[k])] += 1
                        
        #Counts how many circles intersect point min_reach, at the left side of the circle
        #e.g. min_reach = position in X - radius
        #If min_reach is lesser than 0, we would say that the circle intersects at 0
        #Doesn't count if min_reach equals to the center of the circle
        if not max(0, k - A[k]) == k:    
            min_intersect[max(0, k - A[k])] += 1      
    
    #Calculate the prefix sums for max_intersect   
    pref = prefix_sums(max_intersect)   
    
    for k in xrange(N):
        #center + radius
        max_reach = min(N - 1, k + A[k])
        #center - radius
        min_reach = max(0, k - A[k])
        
        #All circles intersected between center and max_reach
        result += max_reach - k
        #All circles intersecting theirs min_reach at this circle max_reach        
        result += min_intersect[max_reach]
        
        #All circles that intersects between ]min_reach, center[
        if k - min_reach > 1:        
            result += pref[k] - pref[min_reach + 1]
        
    if result > 10000000:
        return -1

    return result
    

#prefix sums algorithm
def prefix_sums(A):
    N = len(A)
    pref = [0]*(N + 1)
    
    for k in xrange(1, N + 1):
        pref[k] += pref[k - 1] + A[k - 1]
    
    return pref

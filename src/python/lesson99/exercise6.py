# Name: PolygonConcavityIndex
# Link: https://codility.com/demo/take-sample-test/polygon_concavity_index/


def solution(A):
    N = len(A)
    ccw_array = []
    cw_array = []
    
    for k in xrange(N):
        turn = is_ccw(A[k - 1], A[k], A[(k + 1)%N])
        
        if turn > 0:
            ccw_array.append(k)
        elif turn < 0:
            cw_array.append(k)
            
    if len(ccw_array) == 0 or len(cw_array) == 0:
        return -1
    elif len(cw_array) < len(ccw_array):
        return cw_array[0]
    
    return ccw_array[0]

def is_ccw(p1, p2, p3):
    return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)

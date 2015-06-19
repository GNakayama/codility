def solution(A):
    N = len(A)
    leader, total = goldenLeader(A)
    count = 0
    result = 0
    
    for k in xrange(N - 1):
        if A[k] == leader:
            count += 1 
             
        if count > (k + 1)//2 and (total - count) > (N - (k + 1))//2:
            result += 1

    return result

def goldenLeader(A):
    n = len(A)
    size = 0
    index = -1
    count = 0

    for k in xrange(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1

    if (size > 0):
        candidate = value

        for k in xrange(n):
            if (A[k] == candidate):
                count += 1

    if (count > n // 2):
        return candidate, count

    return -1, -1

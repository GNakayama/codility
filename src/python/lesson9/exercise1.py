def solution(N, P, Q):
    M = len(P)
    result = [0]*M
    pref = pref_semiprimes(P, Q, N)

    for k in xrange(M):
        result[k] = pref[Q[k] + 1] - pref[P[k]]
  
    return result
    
def pref_semiprimes(P, Q, N):
    pref = [0]*(N + 2)
    factors = calc_factors(N)
    
    for  k in xrange(1, N + 2):
        p1 = factors[k - 1]
        
        if (not p1 == 0) and factors[(k - 1)/p1] == 0:
            pref[k] += pref[k - 1] + 1
        else:
            pref[k] += pref[k - 1]
            
    return pref
        
def calc_factors(N):
    factors = [0]*(N + 1)
    
    i = 2
    
    while (i * i <= N):
        if (factors[i] == 0):
            k = i * i
    
            while (k <= N):
                if (factors[k] == 0):
                    factors[k] = i;
                k += i
        i += 1
    
    return factors

def solution(S, P, Q):
    pref = prefix_sums(S)
    M = len(P)
    result = [0]*M
    
    for k in xrange(M):                
        if (pref[0][Q[k] + 1] - pref[0][P[k]]) > 0:
            result[k] = 1   
        elif (pref[1][Q[k] + 1] - pref[1][P[k]]) > 0:
            result[k] = 2
        elif (pref[2][Q[k] + 1] - pref[2][P[k]]) > 0:
            result[k] = 3
        else:
            result[k] = 4
                        
    return result


def prefix_sums(A):
    N = len(A)
    P_3 = [0]*(N + 1)
    P_2 = [0]*(N + 1)
    P_1 = [0]*(N + 1)
    
    for k in xrange(1, N + 1):
        val = impact_factor(A[k - 1])
        P_3[k] = P_3[k - 1] + (val%4)/3
        P_2[k] = P_2[k - 1] + ((val%4)%3)/2
        P_1[k] = P_1[k - 1] + ((val%4)%3)%2
    
    return [P_1, P_2, P_3]
    

def impact_factor(nucleotide):
    if nucleotide == "A":
        return 1
    elif nucleotide == "C":
        return 2
    elif nucleotide == "G":
        return 3
    elif nucleotide == "T":
        return 4
    
    return None

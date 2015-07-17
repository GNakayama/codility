# Name: GenomicRangeQuery
# Link: https://codility.com/demo/take-sample-test/genomic_range_query/


def solution(S, P, Q):
    pref = prefix_sums(S)
    M = len(P)
    result = [0]*M

    # Check the ocurrencxe of the minimal factor for each factor
    for k in xrange(M):
        # Check is there is any occurence of factor A, on the given range
        if (pref[0][Q[k] + 1] - pref[0][P[k]]) > 0:
            result[k] = 1
        # Check is there is any occurence of factor C, on the given range
        elif (pref[1][Q[k] + 1] - pref[1][P[k]]) > 0:
            result[k] = 2
        # Check is there is any occurence of factor G, on the given range
        elif (pref[2][Q[k] + 1] - pref[2][P[k]]) > 0:
            result[k] = 3
        # If none of the above is true then, the query has only T factor
        else:
            result[k] = 4

    return result


# Prefix Sum, sume the occurences of each factor in separated prefix sum Arrays
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

# Translate each nucleotide for it's factor
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


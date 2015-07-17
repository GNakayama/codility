# Name: CountDiv
# Link: https://codility.com/demo/take-sample-test/count_div/


def solution(A, B, K):
    # B//K Al numbers divisible by K from 0 to B, (A - 1)//K 
    # all number divisible by K except A if A is divisible
    return B//K - (A - 1)//K

# Name: BinaryGap
# Link: https://codility.com/demo/take-sample-test/binary_gap/


def solution(N):
    result = 0
    gap = 0
    
    while N%2 == 0:
        N //= 2
    
    while N > 0:
        if N%2 == 0:
            gap += 1
        else:
            result = max(result, gap)
            gap = 0

        N //= 2
    
    return result

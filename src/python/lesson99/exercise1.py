# Name: StrSymmetryPoint
# Link: https://codility.com/demo/take-sample-test/str_symmetry_point/


def solution(S):
    N = len(S)
    result = N//2
    
    if N%2 == 0:
        return -1
    
    front = 0
    back = N - 1
    
    while front < back:
        if not S[front] == S[back]:
            return -1
    
        front += 1
        back -= 1
        
    return result

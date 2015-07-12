# Name: FrogJmp
# Link: https://codility.com/demo/take-sample-test/frog_jmp/


def solution(X, Y, D):
    # Calcs the integer part of the division, distance to be traveled by jump size, if the division leaves a rest, add 1 to the result.
    return ((Y - X)//D) + (1 if (Y - X)%D > 0 else 0)

# Name: TapeEquilibrium
# Link: https://codility.com/demo/take-sample-test/tape_equilibrium/


def solution(A):
    N = len(A)
    total = sum(A)
    left_sum = A[0]
    result = abs(2 * left_sum - total)

    for P in range(2, N):
        # For each loop calculates the sum A[0] + ... + A[P - 1]
        left_sum += A[P - 1]
        # Calculates the difference |A[0] + ... + A[P - 1] - (A[P] + ... + A[N - 1])|
        diff = abs(2 * left_sum - total)

        # If found a new lower diff result equals this diff
        result = min(result, diff)

    return result

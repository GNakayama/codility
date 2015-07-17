# Name: PassingCars
# Link: https://codility.com/demo/take-sample-test/passing_cars/


def solution(A):
    N = len(A)
    result = 0
    count_zero = 0

    for k in xrange(N):
        # Count the numbers of cars going
        if A[k] == 0:
            count_zero += 1
	# For each car coming add the numbers of cars going before
        else:
            result += count_zero
        # -1 if result over 1,000,000,000
        if result > 1000000000:
            return -1

    return result

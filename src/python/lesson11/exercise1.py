def solution(A, B):
    L = len(A)
    result = [0]*L
    fib = fibonacciDynamic(L + 1)
    
    for k in xrange(L):
        result[k] = fib[A[k] + 1] & ((1 << B[k]) - 1)
    return result

def fibonacciDynamic(n):
    fib = [0] * (n + 2)
    fib[1] = 1

    for i in xrange(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) & ((1 << 30) - 1)

    return fib

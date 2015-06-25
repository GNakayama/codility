def solution(A):
    N = len(A)
    index = 0
    discovered = [(-1,0)]

    fib = calc_fib(N + 1)
 
    while True:
        if index == len(discovered):
            return -1
 
        pos = discovered[index][0]
        jumps = discovered[index][1]
        
        index += 1
        
        for offset in fib:
            if pos + offset == N:
                return jumps + 1
            elif pos + offset > N or A[pos + offset] == 0:
                continue
 
            discovered += [(pos + offset, jumps + 1)]
            A[pos + offset] = 0

def calc_fib(N):
    fib = [0] * (N + 2)
    fib[1] = 1
    for i in xrange(2, N + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] > N:
            return fib[i-1: 1: -1]
        elif fib[i] == N:
            return fib[i: 1: -1]

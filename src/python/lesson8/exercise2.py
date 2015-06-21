def solution(N):
    return divisors(N)

def divisors(n):
    i = 1
    result = 0
    
    while (i * i < n):
        if (n % i == 0):
            result += 2
        i += 1

    if (i * i == n):
        result += 1
    
    return result

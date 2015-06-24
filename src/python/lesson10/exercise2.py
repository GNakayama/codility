def solution(A, B):
    Z = len(A)
    result = 0
    
    for k in xrange(Z):
        if has_same_primes(A[k], B[k]):
            result += 1
            
    return result

def has_same_primes(a, b):  
    if a == b:
        return True
    else:        
        if (b%a == 0 and a%(b/a) == 0) or (a%b == 0 and b%(a/b) == 0):
            return True
        
        a_aux = a
        
        while True:            
            c = gcd(a, b, 1)
            
            if c == 1:                 
                return False
            
            while a%c == 0:
                a /= c
            
            if a == 1:
                break
        
        a = a_aux
        
        while True:            
            c = gcd(a, b, 1)
            
            if c == 1:                 
                return False
            
            while b%c == 0:
                b /= c
            
            if b == 1:
                break
    
    return True
            

def gcd(a, b, res):
    if a == b:
        return res * a
    elif (a % 2 == 0) and (b % 2 == 0):
        return gcd(a // 2, b // 2, 2 * res)
    elif (a % 2 == 0):
        return gcd(a // 2, b, res)
    elif (b % 2 == 0):
        return gcd(a, b // 2, res)
    elif a > b:
        return gcd(a - b, b, res)
    else:
        return gcd(a, b - a, res)

def solution(A):
    N = len(A)
    result = 0
    elements_stack = stack(N)
    
    for back in xrange(N):
        if A[back] < 0:
            if back == 0 or not A[back] == A[back - 1]:
                result += 1
                elements_stack.push(A[back])
        elif A[back] == 0 and not A[back] == A[back - 1]:
            result += 1
        elif not elements_stack.size == 0 and not A[back] == A[back - 1]:
                while not elements_stack.size == 0 and A[back] > abs(elements_stack.head()):
                    elements_stack.pop()
                
                if elements_stack.size == 0 or A[back] < abs(elements_stack.head()):
                    result += 1
        elif back == 0 or not A[back] == A[back - 1]:
            result += 1
            
            
    return result
    
class stack(object):
    def __init__(self, N):
        self.size = 0
        self._stack_ = [0] * N

    def push(self, x):
        self._stack_[self.size] = x
        self.size += 1

    def pop(self):
        self.size -= 1
        return self._stack_[self.size]
    
    def head(self):
        return self._stack_[self.size - 1]

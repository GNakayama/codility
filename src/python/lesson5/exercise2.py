def solution(A, B):
    N = len(A)
    direction = 0
    fish = 0
    result = 0
    fish_stack = stack(N)
    
    for k in xrange(N):
        if B[k] == 0 and direction == 0:
            result += 1
        elif B[k] == 0 and direction == 1:
            if A[fish] > A[k]:
                continue
            else:
                result += 1
                direction = 0
                
                while fish_stack.size > 0:
                    head = fish_stack.pop()
                    
                    if A[k] < head:
                        fish_stack.push(head)
                        direction = 1
                        result -= 1
                        break
                    
        elif B[k] == 1 and direction == 0:
            direction = 1
            fish = k
            fish_stack.push(A[k])
        elif B[k] == 1 and direction == 1:
            fish = k
            fish_stack.push(A[k])
            
    return result + fish_stack.size
    

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

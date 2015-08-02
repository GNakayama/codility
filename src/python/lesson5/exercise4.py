# Name: Brackets
# Link: https://codility.com/demo/take-sample-test/brackets/


def solution(S):
    N = len(S)
    symbol_stack = stack(N//2 + 1)    
    
    for k in xrange(N):
	# Push if he have a (, [ or {
        if S[k] == '{' or S[k] == '[' or S[k] == '(':
	    # If we have a stack with half of the size of S the others chars must be ), ], or }
            if symbol_stack.size == N//2 + 1:
                return 0
                
            symbol_stack.push(S[k])
	# Pop the stack for ), ], }
        else:
	    # If the stack is empty, S can't be properly nested
            if symbol_stack.size == 0:
                return 0
            
            head = symbol_stack.pop()
            
	    # If the head os the stack is different form the curretn reversed symbol S is not properly nested.
            if (not (head == '{' and S[k] == '}')) and (not (head == '[' and S[k] == ']')) and (not (head == '(' and S[k] == ')')):
                return 0

    # If there if left elements at the stack at the end of the iteration S is not properly nested    
    if symbol_stack.size > 0:
        return 0
    # If we reach this point S is properly nested
    return 1
    

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

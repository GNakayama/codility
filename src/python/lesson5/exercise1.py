# Name: Nesting
# Link: https://codility.com/demo/take-sample-test/nesting/


def solution(S):
    N = len(S)
    size = 0
    
    # Works as a stack where ( pushes an element, and ) pops one
    for k in xrange(N):
        if S[k] == '(':
            size += 1
        else:
            size -= 1
        
	# If it try to pop an empty stack, error.
        if size < 0:
            return 0
    
    # If the stack is empty at the end of processing the string, string is properly nested
    if size == 0:
        return 1
    else:
        return 0

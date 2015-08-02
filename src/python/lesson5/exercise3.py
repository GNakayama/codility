# Name: StoneWall
# Link: https://codility.com/demo/take-sample-test/stone_wall/


def solution(H):
    N = len(H)
    result = 0
    lower = 0

    height_stack = stack(N)
    height_stack.push(H[0])
    result += 1

    for k in xrange(1, N):
	# If the height of the wall grows we have to use another block
        if H[k] > height_stack.head():
            height_stack.push(H[k])
            result += 1
	# If the height of the wall decreases we have to check is there is a block with the same size as the required
        elif H[k] < height_stack.head():
            height_stack.pop()

	    # If H[k] is smaller than the current head keep looking
            if H[k] < height_stack.head():
                while H[k] < height_stack.head():
                    height_stack.pop()
			
		    # If the stack is empty we have to use a new block
                    if height_stack.size == 0:
                        height_stack.push(H[k])
                        result += 1
                        break
	    	    # If H[k] is greater than the head there is no way to use a block so we have to use a new one
                    elif H[k] > height_stack.head():
                        height_stack.push(H[k])
                        result += 1
                        break
	    # If H[k] is greater than the head there is no way to use a block so we have to use a new one
            elif H[k] >  height_stack.head():
                height_stack.push(H[k])
                result += 1

    return result


# Stack implementation
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

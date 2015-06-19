def solution(H):
    N = len(H)
    result = 0
    lower = 0

    height_stack = stack(N)
    height_stack.push(H[0])
    result += 1

    for k in xrange(1, N):
        if H[k] > height_stack.head():
            height_stack.push(H[k])
            result += 1
        elif H[k] < height_stack.head():
            height_stack.pop()

            if H[k] < height_stack.head():
                while H[k] < height_stack.head():
                    height_stack.pop()

                    if height_stack.size == 0:
                        height_stack.push(H[k])
                        result += 1
                        break
                    elif H[k] > height_stack.head():
                        height_stack.push(H[k])
                        result += 1
                        break
            elif H[k] >  height_stack.head():
                height_stack.push(H[k])
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

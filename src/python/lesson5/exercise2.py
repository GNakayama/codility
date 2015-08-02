# Name: Fish
# Link: https://codility.com/demo/take-sample-test/fish/


def solution(A, B):
    N = len(A)
    # The direction of the last fish
    direction = 0
    # The index of the last fish going downstream
    last_downstream = 0
    #Holds the number of alive fishes going upstream
    upstream = 0
    #Holds the alive fishes going from downstream
    downstream = stack(N)

    for k in xrange(N):
        # If the last fish is going upstream, this means that there is no fish before it going downstream
        if B[k] == 0 and direction == 0:
            upstream += 1
        # The fish k is going on the oposite direction of the last fish going downstream
        elif B[k] == 0 and direction == 1:
            # If the fish going downstream is bigger, then it eats the smaller fish and keep going
            if A[last_downstream] > A[k]:
                continue
            # Otherwise the other fish eats the one going downstream
            else:
                # We add the new fish to the ones going upstream
                upstream += 1
                # Update the direction of the last fish
                direction = 0
                
                # If there is more fishes going downstream we compare the sizes
                while downstream.size > 0:
                    head = downstream.pop()
                    
                    # If there is a bigger fish going downstream, we subtract one from the result and change the direction
                    if A[k] < head:
                        downstream.push(head)
                        direction = 1
                        upstream -= 1
                        break
        # If fish is going downstream update the direction and push it to the stack
        elif B[k] == 1:
            direction = 1
            last_downstream = k
            downstream.push(A[k])

    # The result is the fishes going upstream plus the ones goind downstream
    return upstream + downstream.size


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


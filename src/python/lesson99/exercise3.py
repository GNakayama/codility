# Name: TreeHeight
# Link: https://codility.com/demo/take-sample-test/tree_height/


def solution(T):
    height = -1
    visited = 0
    
    if not T:
        return -1
    
    return calc_height(T, height)

def calc_height(root, height):
    height += 1
    height_left = height
    height_right = height
    
    if root.l:
        height_left = calc_height(root.l, height) 
    if root.r:
        height_right = calc_height(root.r, height) 
        
    return max(height_left, height_right)


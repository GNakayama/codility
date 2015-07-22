# Name: ArrayInversionCount
# Link: https://codility.com/demo/take-sample-test/array_inversion_count/


def solution(A):
    result = mergeSort(A, 0)

      
    if result > 1000000000:
        return -1
        
    return result

def mergeSort(alist, count):    
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        count = mergeSort(lefthalf, count)
        count = mergeSort(righthalf, count)
    
        i = 0
        j = 0
        k = 0   
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
                count += j
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
            count += j

        while j < len(righthalf):
            alist[k] = righthalf[j]                
            j = j + 1
            k = k + 1
            
    return count    
        

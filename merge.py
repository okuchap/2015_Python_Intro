def merge(left, right, compare):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1
    
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1

import operator

def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        print right
        print left
        return merge(left, right, compare)

L2 = [8,3,5,2,541,4]

mergeSort(L2)

print L2
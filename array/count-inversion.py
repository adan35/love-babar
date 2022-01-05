
def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    
    a = arr[:len(arr)//2]         
    b = arr[len(arr)//2:]
    
    a, ai = mergeSortInversions(a)
    b, bi = mergeSortInversions(b)
    
    i = j = 0
    c = []   
    inversions = 0 + ai + bi 

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += len(a)-i
            
    c += a[i:]
    c += b[j:]
        
    return c, inversions

a = [2,3,4,2,1,0]

print(mergeSortInversions(a))

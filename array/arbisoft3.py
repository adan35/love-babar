def longRunningFunction(array):
    count = 0
    for i in range(0,len(array)):
        idx = i
        for j in range(i + 1,len(array)):
            count += 1
            if ( array[idx] > array[j] ):
                idx = j
        
        array[i], array[idx] = array[idx], array[i]
        
    return count 

a = [2,2,8,14]
print(longRunningFunction(a))

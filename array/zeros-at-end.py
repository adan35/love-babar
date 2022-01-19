def zerosAtEnd(arr):
    
    count0 = 0
    c = []
    
    for a in arr:
        if a == 0:
            count0 += 1
        else:
            c.append(a)
            
    for _ in range(count0):
        c.append(0)
        
    return c

arr = [-1, 0 ,1, 2, 0, 3, 0, 5]
print(zerosAtEnd(arr))


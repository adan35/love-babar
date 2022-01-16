def median(a):
    
    sort = sorted(a)
    
    if len(sort) % 2 == 0:
        return sort[(len(sort) // 2) - 1]
    else:
        return sort[len(sort) // 2]
    
a = [90, 100, 78, 89, 67]
print(median(a))


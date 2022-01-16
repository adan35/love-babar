def binarySearch(a, x):
    begin = mid = 0
    last = len(a) - 1
    
    count = 0
    
    while begin <= last:
        count += 1
        mid = (begin+last)//2
        if a[mid] < x:
            begin = mid + 1
            
        elif a[mid] > x:
            last = mid -1
        
        else:
            return mid, count
    
    return -1, count

a = [14, 96, 129, 134, 158, 206, 222, 264, 376, 397, 507, 552, 572, 592, 744, 759, 794, 817, 864, 872, 889, 916, 974, 988]
print(binarySearch(a, 129))
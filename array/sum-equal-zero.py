def subArrayExists(a):
    
    sum = 0
    s = set()

    for i in range(len(a)):
        sum += a[i]
        
        if sum == 0 or sum in s:
            return True
        
        s.add(sum)
    
    return False

a = [4, 2, -3, 1, 6]
print(subArrayExists(a))
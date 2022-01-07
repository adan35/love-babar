def findLongestConsectiveSequence(a):
    
    a = sorted(a)
    max_count = count = i = 0
    
    while i < len(a)-1:
        
        if a[i] == a[i+1] - 1:
            count += 1
        else:
            count = 0
        i += 1
        
        if max_count < count:
            max_count = count
            
    return max_count + 1

a = [1,9,3,10,4,20,2]
print(findLongestConsectiveSequence(a))
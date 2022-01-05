def rearrangeNumbers(a):
    sorted_a = sorted(a)
    
    for i in range(len(sorted_a)):
        if sorted_a[i] >= 0:
            first_pos_index = i
            break
        
    pos = sorted_a[first_pos_index:]
    neg = sorted_a[:first_pos_index]
    c = []
    
    i, j = 0, len(neg)-1
    while i < len(pos) and j >= 0:
        c.append(pos[i])
        c.append(neg[j])
        i += 1
        j -= 1
        
    while i < 0:
        c.append(pos[i])
        i += 1
    
    while j >= 0:
        c.append(neg[j])
        j -= 1    
        
    return c
    
a = [1, 2, 3, -2, -4, -2, -1, -9]
print(rearrangeNumbers(a))
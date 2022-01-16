from operator import le


def median_of_two_sorted_arrays(a, b):
    
    i = j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            
    c += a[i:]
    c += b[j:]
    
    if len(c) % 2 == 0:
        return c[(len(c) // 2) - 1]
    
    return c[len(c) // 2]

a = [-5, 3, 6, 12, 15]
b = [-12, -10, -6, -3, 4, 10]

print(median_of_two_sorted_arrays(a, b))
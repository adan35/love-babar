def kthMin(a, k):
    min = 9999999
    for i in range(0, k, 1):
        if (a[i] < min):
            min = a[i]
    return min

def kthMax(a, k):
    max = -9999999
    for i in range(0, k, 1):
        if (a[i] > max):
            max = a[i]
    return max

a = [1,2,3,0,5]
print(kthMin(a, 3))
print(kthMax(a, 3))
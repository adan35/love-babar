def movNegative(a):
    j = len(a)-1
    for i in range(0, len(a), 1):
        if (i == j): return a

        if (a[i] < 0):
            a[i], a[j] = a[j], a[i]
            j -= 1
    return a

a = [-1,2,3,-4,0]
print(movNegative(a))

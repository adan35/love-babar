def maxDiff(a, k):
    n = len(a)
    if n == 1:
        return 0

    ans = a[n-1] - a[0]

    sorted(a)
    big = a[n-1] - k
    small = a[0] + k
    if big < small:
        big, small = small, big
    for i in range(1, n-1, 1):
        add = a[i] + k
        sub = a[i] - k
        # if add is smaller than big then it is useless, if sub is greater 
        # then small. Because we want max and min value after adding or 
        # subtracting k 
        if sub >= small or add <= big:
            continue
        # we want minimum distance so 
        if sub - small <= big - add:
            small = sub
        else:
            big = add

    return min(ans, big - small)

a = [1, 5, 10, 15]
k = 3

print(maxDiff(a, k))
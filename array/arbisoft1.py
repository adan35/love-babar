def min_jumps(arr, start, end):

    if(start == end):
        return 0

    min = 999999 
    idx = 1

    while (arr[start] >= idx) and (end >= start + idx):

        jumps = min_jumps(arr, start + idx, end) + 1
        if(min > jumps):
            min = jumps

    return min;


arr = [1, 1, 1, 3, 2, 3, 4, 2, 1, 2]
ans = min_jumps(arr, 0, len(arr)-1)
print(ans)

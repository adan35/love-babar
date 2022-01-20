from audioop import findfactor


def findFrequency(arr, x):
    
    count = 0
    for a in arr:
        if a == x:
            count += 1

    return count


arr = [1, 1, 1, 1, 1, 1]
print(findFrequency(arr, 1))
    
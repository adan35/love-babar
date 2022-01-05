
def getPairCount(a, sum):
    count = 0
    
    for i in range(len(a)-1):
        for j in range(1+i, len(a)):
            if a[i] + a[j] == sum:
                count += 1
    
    return count

a = [1, 5, 7, -1]
print(getPairCount(a, 6))
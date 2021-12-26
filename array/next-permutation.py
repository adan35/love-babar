def nextPermutation(a):
    for i in range(len(a)-2, -1, -1):
        if a[i] < a[i+1]:
            index1 = i
            break

    for i in range(len(a)-1, -1, -1):
        if a[i] > a[index1]:
            index2 = i
            break

    a[index1], a[index2] = a[index2], a[index1]

    l = []

    for i in range(len(a)-1, index1, -1):
        l.append(a[i])

    count = 0
    for i in range(index1+1, len(a)):
        a[i] = l[count]
        count += 1

    return a

a = [1, 3, 2]
print(nextPermutation(a))

def sort012(a):
    count0 = count1 = count2 = 0
    c0 = c1 = c2 = 0
    for i in a:
        if i == 0:
            count0 += 1
        if i == 1:
            count1 += 1
        if i == 2:
            count2 += 1

    for i in range(0, len(a), 1):
        if (c0 < count0):
            a[i] = 0
            c0 += 1

        elif (c1 < count1):
            a[i] = 1
            c1 += 1

        elif (c2 < count2):
            a[i] = 2
            c2 += 1


    return a

a = [0,0,1,0,1,2,1,2]

print(sort012((a)))

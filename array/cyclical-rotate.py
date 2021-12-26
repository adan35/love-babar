def rotate(a):
    temp = a[-1]
    for i in range(len(a)-1, 0, -1):
        a[i] = a[i-1]
    a[0] = temp
    print(a)

a = [1,2,3,4,5]
rotate(a)

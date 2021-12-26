def mergeOverlappingIntervals(a):
    flag = False
    is_last = False
    _list = []
    for i in range(len(a)-1):
        l = []

        if flag:
            flag = False
            continue

        if a[i][1] >= a[i+1][0]:
            if i+1 == len(a)-1:
                is_last = True
            l.append(a[i][0])
            l.append(a[i+1][1])
            flag = True
        else:
            l.append(a[i][0])
            l.append(a[i][1])

        _list.append(l)
        
    if not is_last:
        _list.append(a[len(a)-1])

    return _list

a = [[1,3], [2,4], [5,7], [6,8], [10,13], [14,15]]

print(mergeOverlappingIntervals(a))
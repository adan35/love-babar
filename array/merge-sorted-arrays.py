def mergeSortedArrays(a, b):

    lst = []

    ai = bi = 0

    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            lst.append(a[ai])
            ai += 1
        else:
            lst.append(b[bi])
            bi += 1

    while ai < len(a):
        lst.append(a[ai])
        ai += 1

    while bi < len(b):
        lst.append(b[bi])
        bi += 1

    return lst

a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]

print(mergeSortedArrays(a, b))
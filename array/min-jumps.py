def minJumps(a):
    count = j = i = 0
    while i < len(a):
        if a[i] <= 0:
            return -1

        if i == 0:
            j = a[i]

        if j >= len(a) - 1:
            count += 1
            break

        i = a[j]
        j += i
        count += 1

    return count

a = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
b = [2, 3, 5, 8, 9, 2, 6, 3, 6, 8, 9]
c = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(minJumps(a))
print(minJumps(b))
print(minJumps(c))
from collections import Counter

def findCommon(a, b, c):
    c1 = Counter(a)
    c2 = Counter(b)
    c3 = Counter(c)
    c = []

    for key in c1.keys():
        if c2[key] > 0 and c3[key] > 0:
            mini = min(c1[key], c2[key], c3[key])
            for _ in range(mini):
                c.append(key)
                
    return c

a = [1, 5, 5]
b = [3, 4, 5, 5, 10]
c = [5, 5, 10, 20]

print(findCommon(a, b, c))
from collections import Counter

def isSubset(a1, a2):
    c1 = Counter(a1)
    c2 = Counter(a2)

    for k in c2.keys():
        if c1[k] > 0:
            continue
        else:
            return False
        
    return True

a1 = [11, 1, 13, 21, 3, 7]
a2 = [11, 3, 7, 2]
print(isSubset(a1, a2))
    
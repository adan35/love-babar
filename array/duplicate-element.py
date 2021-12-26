from collections import Counter

def duplicateElement(a):
    lst = []
    c = Counter(a)
    for key in c.keys():
        if c[key] > 1:
            lst.append(key)
    return lst

a = [1, 2, 3, 4 ,3]
print(duplicateElement(a))
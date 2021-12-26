from collections import defaultdict, Counter
# union with deafultdict
def union(a1, a2):
    dic = defaultdict(int)
    a = []
    for i in a1:
        a.append(i)
    for i in a2:
        a.append(i)
    
    for i in a:
        dic[i] += 1
    
    for i in dic.keys():
        print(i, end=' ')
# union with counter
def union2(a1, a2):
    a = []
    for i in a1:
        a.append(i)
    for i in a2:
        a.append(i)

    c = Counter(a)
    print(c.keys())

def intersection(a1, a2):
    a = []
    for i in a1:
        a.append(i)
    for i in a2:
        a.append(i)
    
    c = Counter(a)
    for keys in c.keys():
        if (c[keys] > 1):
            print(keys, end=' ')



a1 = [2,3,4,5,6]
a2 = [2,4,8,16]

union2(a1, a2)
intersection(a1, a2)
from collections import Counter
    
def find_all_elements(a, k):
    c = Counter(a)
    ratio = len(a) // k
    for key in c.keys():
        if c[key] >= ratio:
            print(key, end=' ')

a = [1, 2, 3, 4, 5, 5, 3, 3]
k = 4
find_all_elements(a, k)
def mini(s):
    return min(s)

def maxi(s):
    return max(s)

def mini2(s):
    min = 99999
    for i in s:
        if (i < min):
            min = i
    return min

def maxi2(s):
    max = -99999
    for i in s:
        if (i > max):
            max = i
    return max

s = [1,2,3,4,0,5]
print(mini(s))
print(maxi(s))
print(mini2(s))
print(maxi2(s))
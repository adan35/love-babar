def trappingWater(a):
    
    water = 0
    mini = min(a[0], a[len(a)-1])
    for i in range(1, len(a)-1):
        if mini - a[i] >= 0:
            water += mini - a[i]
    return water


a = [8, 8, 2, 4, 5, 5, 1]
print(trappingWater(a))


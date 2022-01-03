def merge(a, l, m, h):
    list_ = []
    list1 = a[l:m+1]
    list2 = a[m+1:h+1]
    i = p = q = count = 0
    
    while i < len(list2):
        if list1[p] < list2[q]:
            list_.append(list1[p])
            p += 1
        else:
            list_.append(list2[q])
            q += 1
        i += 1

    while p < len(list1):
        list_.append(list1[p])
        p += 1
        
    while q < len(list2):
        list_.append(list2[q])
        q += 1
        
    for k in range(l, h+1):
        a[k] = list_[count]
        count += 1
        
        

def mergeSort(a, l, h):
    if l >= h:
        return
    
    m =  (l+h)//2
    mergeSort(a, l, m)
    mergeSort(a, m+1, h)
    merge(a, l, m, h)

a = [2,3,4,2,1,0]
mergeSort(a, 0, len(a)-1)
print(a)

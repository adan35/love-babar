
def isPalindrome(arr):
    
    i, j = 0, len(arr)-1
    c = []
    
    while i < len(arr)//2:
        c.append(arr[i])
        i += 1
        
    count = 0
        
    while count < len(c):
        if arr[j] != c[count]:
            return 0
        count += 1
        j -= 1
        
    return 1
        
        
    
def palindromeArray(arr):
    
    for a in arr:
        if not isPalindrome(str(a)):
            return 0
    
    return 1

a = [111, 222, 333, 444, 5556]
print(palindromeArray(a))
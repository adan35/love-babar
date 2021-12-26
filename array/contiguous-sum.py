from sys import maxsize
def maxSubArraySum(a):
    max_so_far = -maxsize-1
    max_ending_here = 0
    for i in range(0, len(a), 1):
        max_ending_here += a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

a = [-99, -44, -1, 0, 22, 34, -100]
print(maxSubArraySum(a))
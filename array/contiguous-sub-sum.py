from sys import maxsize

def maxSubarraySum(a):
    max_so_far = -maxsize - 1
    max_ending_here = 0
    for i in range(0, len(a)):
        max_ending_here += a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

a = [1,2,3,-2,5]
print(maxSubarraySum(a))
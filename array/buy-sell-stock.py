from sys import maxsize

def maxProfit(prices):
    min, index = maxsize, 0
    for i in range(len(prices)):
        if min > prices[i]:
            min = prices[i]
            index = i
            
    if index >= len(prices):
        return 0
    
    max = -maxsize - 1
    for i in range(index, len(prices)):
        if max < prices[i]:
            max = prices[i]
            
    profit = max - min
    
    if profit < 0:
        return 0
    else:
        return profit
    
a = [7,4,5,3,0,1]
print(maxProfit(a))
    
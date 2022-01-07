def maxSubarrayProduct(a):
    
    max_so_far = 0
    max_product_here = min_product_here = 1
    
    for n in a:
        
        if n > 0:
            max_product_here *= n
            min_product_here = min(min_product_here * n, 1)
            
        elif n == 0:
            max_product_here = 1
            min_product_here = 1
            
        else:
            temp = max_product_here 
            max_product_here = max(min_product_here * n, 1)
            min_product_here = temp * n
            
        if max_so_far < max_product_here:
            max_so_far = max_product_here
        
    return max_so_far
    

a = [6, -3, -10, 0, 2]
print(maxSubarrayProduct(a))
        
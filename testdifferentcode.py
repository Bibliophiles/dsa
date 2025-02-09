def findMinCost(efficiency):
    efficiency.sort()
    n = len(efficiency)
    min_cost = float('inf')
    
    for exclude in range(n):
        cost = 0
        last = None  
        
        for i in range(n):
            if i == exclude:
                continue  
            if last is None:
                last = efficiency[i]
            else:
                cost += efficiency[i] - last 
                last = None  
        
        min_cost = min(min_cost, cost)
    
    return min_cost

efficiency = [4, 1, 2, 8, 9]
result = findMinCost(efficiency)
print(result)  

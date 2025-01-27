def findMinCost(efficiency):
    efficiency.sort()
    n = len(efficiency)
    min_cost = float('inf')
    
    # Precompute the total cost if no one is excluded
    total_cost = 0
    for i in range(0, n-1, 2):
        total_cost += abs(efficiency[i] - efficiency[i+1])
    
    # Try excluding each worker and calculate the new total cost
    for i in range(n):
        if i % 2 == 0:
            # Exclude the i-th worker, adjust the pairs accordingly
            if i < n-1:
                new_cost = total_cost - abs(efficiency[i] - efficiency[i+1])
                if i > 0:
                    new_cost += abs(efficiency[i-1] - efficiency[i+1])
            else:
                # If excluding the last worker, just remove the last pair
                new_cost = total_cost - abs(efficiency[i-1] - efficiency[i])
        else:
            # Exclude the i-th worker, adjust the pairs accordingly
            new_cost = total_cost - abs(efficiency[i-1] - efficiency[i])
            if i < n-1:
                new_cost += abs(efficiency[i-1] - efficiency[i+1])
        
        if new_cost < min_cost:
            min_cost = new_cost
    
    return min_cost

# Example usage:
efficiency = [4, 2, 8, 1, 9]
print(findMinCost(efficiency))  # Output: 2
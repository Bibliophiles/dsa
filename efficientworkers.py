from typing import List

class Solution:
    def findMinCost(self, efficiency : List[int]) -> int:
        efficiency.sort()
        #best solution is preSum and postSum





# Implementation of the function
def findMinCost(efficiency):
    # Sort the efficiencies to minimize pair differences
    efficiency.sort()
    n = len(efficiency)
    
    # Precompute prefix sums
    prefix_sum = [0] * n
    prefix_sum[0] = efficiency[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + efficiency[i]
    
    # Calculate minimum cost by excluding each worker
    min_cost = float('inf')
    for i in range(n):
        # Exclude worker i and pair the remaining workers
        left = efficiency[:i] + efficiency[i+1:]
        
        # Calculate the cost of pairing adjacent workers
        cost = 0
        for j in range(0, len(left), 2):
            cost += abs(left[j] - left[j+1])
        
        # Update the minimum cost
        min_cost = min(min_cost, cost)
    
    return min_cost

# Example usage
efficiency = [4, 2, 8, 1, 9]
findMinCost(efficiency)

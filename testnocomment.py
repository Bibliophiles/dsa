def findMinCost(efficiency):
    n = len(efficiency)
    A = sorted(efficiency)
    
    prefix = [0] * (n + 1)
    prefix[0] = 0
    prefix[1] = 0  
    for i in range(2, n + 1):
        if i % 2 == 0:
            prefix[i] = prefix[i - 2] + (A[i - 1] - A[i - 2])
        else:
            prefix[i] = prefix[i - 1]

    suffix = [0] * (n + 1)
    suffix[n] = 0
    suffix[n - 1] = 0  
    for i in range(n - 2, -1, -1):
        suffix[i] = (A[i + 1] - A[i]) + suffix[i + 2]

    ans = float('inf')
    for k in range(n):
        if k % 2 == 0:
            cost = prefix[k] + (suffix[k + 1] if k + 1 < n else 0)
        else:
            if k + 1 < n:
                cost = prefix[k - 1] + (A[k + 1] - A[k - 1]) + (suffix[k + 2] if k + 2 < n else 0)
            else:
                cost = prefix[k - 1]
        ans = min(ans, cost)

    return ans

# Given efficiency list:
efficiency = [4, 1, 2, 8, 9]
result = findMinCost(efficiency)
print(result)  # Expected output: 2

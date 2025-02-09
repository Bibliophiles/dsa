def findMinCost(efficiency):
    n = len(efficiency)
    # Sort the efficiencies.
    A = sorted(efficiency)

    # Build prefix array.
    # prefix[i] = cost to pair A[0...i-1] when pairing adjacent elements.
    # For an odd number of elements, the last one remains unpaired.
    prefix = [0] * (n + 1)
    prefix[0] = 0
    prefix[1] = 0  # one element, no pair, cost=0.
    for i in range(2, n + 1):
        if i % 2 == 0:
            prefix[i] = prefix[i - 2] + (A[i - 1] - A[i - 2])
        else:
            # If there is an odd number, the last element is left unpaired.
            prefix[i] = prefix[i - 1]

    # Build suffix array.
    # suffix[i] = cost to pair A[i...n-1] in adjacent pairs.
    # If there is an odd number of elements in this segment, the last remains unpaired.
    suffix = [0] * (n + 1)
    suffix[n] = 0
    suffix[n - 1] = 0  # segment of length 1 has no pairing cost.
    for i in range(n - 2, -1, -1):
        suffix[i] = (A[i + 1] - A[i]) + suffix[i + 2]

    # Now try excluding each worker at index k.
    ans = float('inf')
    for k in range(n):
        if k % 2 == 0:
            # Left segment has an even count.
            cost = prefix[k] + (suffix[k + 1] if k + 1 < n else 0)
        else:
            # Left segment has an odd count.
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

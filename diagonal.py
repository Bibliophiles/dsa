def diagonalDifference(arr):
    arrayLen = len(arr)    
    left = 0
    right = 0
    for n in range(arrayLen):
        left += arr[n][n]
    for j in range(arrayLen):
        right += arr[j][arrayLen-j-1]
    diff = abs(left - right)
    return diff


def diagonalDifference(arr):
    return abs(sum(arr[i][i] - arr[i][-i-1] for i in range(len(arr))))


def diagonalDifference(arr):
    arrayLen = int(len(arr))    
    diff = 0
    for n in range(arrayLen):
        diff += arr[n][n] - arr[n][arrayLen-n-1]
    return abs(diff)

def diagonalDifference(arr):
    arrayLen = int(len(arr))    
    diff = 0
    for n in range(arrayLen):
        diff += arr[n][n] - arr[n][-n-1]
        
    return abs(diff)


def diagonalDifference(arr):
    arrayLen = int(len(arr))    
    diff = 0
    for n in range(arrayLen):
        diff += arr[n][n] - arr[n][-1-n]
        
    return abs(diff)
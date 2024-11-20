def findMedian(arr):
    return sorted(arr)[(len(arr) - 1) // 2]



def findMedian(arr):
    arrLen = len(arr)
    sortArr = sorted(arr)

    median = (arrLen + 1) / 2
    return sortArr(median - 1)
def countingSort(arr): 
        counter = [0]*100
        for a in arr:
            counter[a] += 1

        return counter
        


def countingSort(arr):
    return [arr.count(i) for i in range(100)]

arr = [1,3,3]
arrLen = len(arr)
#print([arr.count(i) for i in range(25)])

values = sum(1 for num in arr)
print(values)
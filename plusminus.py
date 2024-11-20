def plusMinus(arr):
    positive_values = sum(1 for num in arr if num > 0)
    negative_values = sum(1 for num in arr if num < 0)
    zero_values = len(arr) - positive_values - negative_values

    positive_ratios = positive_values / len(arr)
    negative_ratios = negative_values / len(arr)
    zero_ratios = zero_values / len(arr)

    print(positive_ratios)
    print(negative_ratios)
    print(zero_ratios)

print(plusMinus([1,1,0,-1, -2]))
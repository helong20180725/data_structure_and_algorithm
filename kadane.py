def kadane(array):
    """
    Search for a subarray which has the maximum sum in a non-empty array.
    """
    curSum = maxSum = float('-inf')

    for x in array:
        curSum = x + max(curSum, 0)

        maxSum = max(curSum, maxSum)

        print("x: {:5},   curSum: {:5},   maxSum: {:5}".format(x, curSum, maxSum))
    
    return maxSum

if __name__ == "__main__":
    array = [1, 2, -3, 2, -1, 2, 5, 30, -23, 9, -8, -10, 2, -9, 8, 4, 5, -1, 0, -2]

    print(kadane(array))
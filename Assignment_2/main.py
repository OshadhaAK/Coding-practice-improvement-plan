def maxSubArray(array):
    maxSum = 0
    for startIndex in range(0, len(array)):
        contiguousSum = 0
        for element in range(startIndex, len(array)):
            contiguousSum += array[element]
            if(contiguousSum > maxSum):
                maxSum = contiguousSum
    return maxSum


nums = [5, 4, -1, 7, 8]
maxSubArray(nums)

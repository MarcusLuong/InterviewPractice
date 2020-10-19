# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.
    
def runningSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    previousSum = 0
    runningSum = []
    for i in range(len(nums)):
        runningSum.append(nums[i]+previousSum)
        previousSum = nums[i]+previousSum 

    return runningSum
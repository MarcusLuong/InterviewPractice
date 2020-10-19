# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



import copy

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    ## create set that excludes nums[i]
    ## check if target - nums[i] is in the set 
    ## if yes, return its position
    ## if no, continue
    for i in range(len(nums)):
        newNums = copy.copy(nums)
        del newNums[i]
        sumTarget = target - nums[i]
        if sumTarget in newNums:
            position1 = i
            position2 = nums.index(sumTarget)
        else:
            continue
    return [position2, position1]

# Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

# An array A is a zigzag array if either:

# Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...

# OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...

# Return the minimum number of moves to transform the given array nums into a zigzag array.
def movesToMakeZigzag(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    movesRequired = []
    for i in range(len(nums)):
        if i == 0:
            if nums[i] >= nums[i+1]:
                movesRequired.append(nums[i]-nums[i+1]+1)
            else:
                movesRequired.append(0)
        elif i == len(nums)-1:
            if nums[i] >= nums [i-1]:
                movesRequired.append(nums[i]-nums[i-1]+1)
            else:
                movesRequired.append(0)
        else:
            if nums[i] >= nums [i-1] or nums[i] >= nums[i+1]:
                movesRequired.append(nums[i]-min(nums[i+1], nums[i-1])+1)
            else:
                movesRequired.append(0)
            
    oddSum = 0
    evenSum = 0
    for i in range(len(movesRequired)):
        if i % 2 == 1:
            oddSum = oddSum + movesRequired[i]
        else:
            evenSum = evenSum + movesRequired[i]
    
    return min(evenSum, oddSum)
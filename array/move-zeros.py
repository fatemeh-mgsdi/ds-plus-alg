# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.


# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


def moveZeroes(nums):

    # // Start with the first position
    insertPosition = 0

    for i in range(0, len(nums)):
        #  Fill all non-zero numbers
        if nums[i] != 0:
            nums[insertPosition] = nums[i]
            insertPosition += 1

    while insertPosition < nums.length:
        insertPosition += 1
        nums[insertPosition] = 0

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.

def removeDuplicates(self, nums):
    if len(nums) == 0:
        return 0

    length = 1
    index = 1
    previous = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != previous:
            length += 1
            previous = nums[i]
            nums[index] = nums[i]
            index += 1

    return length
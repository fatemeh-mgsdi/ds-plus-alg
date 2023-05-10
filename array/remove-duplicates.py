# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such
# that each unique element appears only once. The relative order of the elements should be kept the same

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

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
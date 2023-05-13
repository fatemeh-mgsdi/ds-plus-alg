# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbers(self, nums):
    length_nums = len(nums)
    all_numbers_set = set(range(1, length_nums + 1))

    for num in nums:
        if num in all_numbers_set:
            all_numbers_set.remove(num)

    return list(all_numbers_set)
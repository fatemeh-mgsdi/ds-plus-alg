from typing import List


def search(nums: List[int], target: int) -> int:

    low = 0
    high = len(nums) - 1

    while low<=high:
        mid = int( (low+ high)/ 2)
        guess = nums[mid]
        if guess == target:
            return mid

        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1




nums = [-1,0,3,5,9,12]
target = 12
print(search(nums, target))
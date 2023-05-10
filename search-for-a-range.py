from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        begin = -1
        end = -1
        # Find the first occurrence of target in A
        front = len(nums) - 1
        back = 0
        while back <= front:
            mid = (front + back) // 2
            if nums[mid] > target:
                front = mid - 1
            elif nums[mid] < target:
                back = mid + 1
            else:
                front = mid - 1
                begin = mid
        # Target is not found in the array A
        if begin == -1:         return [-1, -1]
        # Find the last occurrence of target in A
        front = len(nums) - 1
        back = 0
        while back <= front:
            mid = (front + back) // 2
            if nums[mid] > target:
                front = mid - 1
            elif nums[mid] < target:
                back = mid + 1
            else:
                back = mid + 1
                end = mid
        return [begin, end]
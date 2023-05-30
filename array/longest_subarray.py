# Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.

def find_length(nums, k):
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans


find_length([3, 1, 2, 7, 4, 2, 1, 1, 5] , 8)
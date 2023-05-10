# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.


# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeroes(arr):

    i = 0
    j = len(arr) - 1

    while i<len(arr) and j>0:
        if arr[i] == 0:
            arr.pop(i)
            arr.insert(j, 0)
            j -= 1
        else:
            i += 1

    print(arr)


moveZeroes([0, 0, 1])



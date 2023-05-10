# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

def find_ones(arr):
    max_ones = 0
    counter = 0

    for item in arr:
        if item == 1:
            counter += 1
            if max_ones<counter:
                max_ones = counter
        else:
            counter = 0
    return max_ones

print(find_ones([1,0,1,1,0,1]))
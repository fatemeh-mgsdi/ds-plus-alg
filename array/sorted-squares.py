# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

def sorted_squares(arr):
    index = len(arr) -1
    right = len(arr) -1
    left = 0

    new_list = [0 for i in arr]

    while right >= left:
        if abs(arr[right]) >= abs(arr[left]):
            new_list[index] = arr[right] * arr[right]
            right -= 1

        elif abs(arr[right]) < abs(arr[left]):
            new_list[index] = arr[left] * arr[left]
            left += 1

        index -= 1

    print(new_list)


sorted_squares([-4,-1,0,3,10])


# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]


def duplicate(arr):
    zero_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1

    j = len(arr) - zero_count
    head = len(arr) - 1

    while j > 0:
        if arr[j] == 0:
            arr[head] = 0
            head -= 1
            arr[head] = 0
        else:
            arr[head] = arr[j]
        head -= 1
        j -= 1
    print(arr)


duplicate([1, 0, 2, 3, 0, 4, 5, 0])

def validMountainArray(arr):

    if len(arr) < 3:
        return False

    is_rising = True
    peak = -1
    rising_count = 0
    bottom = None
    last_item = 0
    for num in arr:
        if num>peak:
            rising_count += 1
            if bottom or not is_rising:
                return False

            peak = num
        elif num == last_item:
            return False
        else:
            if not is_rising and num>last_item : return False
            if not is_rising and num>bottom : return False
            if rising_count < 2:
                return False
            bottom = num
            is_rising = False
        last_item = num

    if is_rising:
        return False

    return True

print(validMountainArray([14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]))
#
# tmp1 = None
# counter = 0
# for i in range(len(arr) - 1):
#     if arr[i] > arr[i + 1]:
#         tmp1 = i
#         break
#     elif arr[i] < arr[i + 1]:
#         counter += 1
#     else:
#         break
#
# if tmp1 is not None and counter >= 1:
#
#     for j in range(tmp1, len(arr) - 1):
#         if arr[j] < arr[j + 1]:
#             return False
#         elif arr[j] == arr[j + 1]:
#             return False
#
#     return True
# else:
#     return False
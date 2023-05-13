# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.


def find_numbers(arr):
    numbers_count = 0
    for num in arr:
        counter = 0
        while num >= 1:
            num = num / 10
            counter += 1

        if counter % 2 == 0:
            numbers_count += 1

    print(numbers_count)




# better solution
def find_numbers(arr):
    arr_str = map(str, arr)
    counter = 0
    for num in arr_str:
        if len(num) % 2 == 0:
            counter += 1
    return counter


find_numbers([555, 901, 482, 1771])

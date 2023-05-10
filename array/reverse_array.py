arr = [1, 4, 3, 2]
start = 0
end = len(arr) - 1

while start<end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    start += 1
    end -= 1

print(arr)

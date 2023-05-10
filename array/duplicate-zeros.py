# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

def duplicate(arr):

    i = 0

    # loop through all dynamic elements
    while i < len(arr)-1:
        # if the character is a zero
        if arr[i]==0:
            # remove the last item from the array
            arr.pop()
            # insert a zero in front of current element
            arr.insert(i+1, 0)
            # move one place forward
            i += 1

        # increment to the next character
        i += 1
    print(arr)

duplicate([1,0,2,3,0,4,5,0])

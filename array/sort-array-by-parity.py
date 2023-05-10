# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#
# Return any array that satisfies this condition.


def sortArrayByParity(self, A):
    if len(A) > 1:
        counter = 0
        odd_counter = 0
        idx = 0

        for num in A:
            if num % 2 != 0:
                odd_counter += 1

        while counter <= odd_counter and idx <= len(A) - 1:
            if A[idx] % 2 != 0:
                number = A[idx]
                A.pop(idx)
                A.append(number)
                counter += 1
            else:
                idx += 1

    return A
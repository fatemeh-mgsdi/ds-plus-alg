# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

def checkIfExist(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    lookup = set()
    for x in arr:
        if 2 * x in lookup or \
                (x % 2 == 0 and x // 2 in lookup):
            return True
        lookup.add(x)
    return False
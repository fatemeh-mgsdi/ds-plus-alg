def thirdMax(self, nums):
    maximum_lists = set()
    for num in nums:
        maximum_lists.add(num)
        if len(maximum_lists) > 3:
            maximum_lists.remove(min(maximum_lists))
    if len(maximum_lists) == 3:
        return min(maximum_lists)
    else:
        return max(maximum_lists)
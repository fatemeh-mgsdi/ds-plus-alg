
    An alternative way to implement Binary Search
    Search Condition needs to access element's immediate left and right neighbors
    Use element's neighbors to determine if condition is met and decide whether to go left or right
    Gurantees Search Space is at least 3 in size at each step
    Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.

 Distinguishing Syntax:

    Initial Condition: left = 0, right = length-1
    Termination: left + 1 == right
    Searching Left: right = mid
    Searching Right: left = mid

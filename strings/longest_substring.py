# You are given a binary substring s (a string containing only "0" and "1"). 
# An operation involves flipping a "0" into a "1". 
# What is the length of the longest substring containing only "1" after performing at most one operation?

# For example, given s = "1101100111", the answer is 5. If you perform the operation at index 2, the string becomes 1111100111.

def find_length(s):
    left = curr = ans = 0 
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans
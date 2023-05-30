from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]



class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        end = s.length-1
        while left < end:
            # swap
            temp = s[left]
            s[left] = s[end]
            s[end] = temp
            
            left += 1
            end -= 1
        

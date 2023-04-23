'''
Given a non-empty integer array, return True if any value appears at least twice in the array, and return False if every element is distinct.
'''

from typing import List
class Solution:
    def ContainsDuplicate(self, nums: List[int]) -> bool: # The function returns a Boolean object.
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n) # The integer is added to the set.
            return False 

'''
Given a non-empty list of anagrams consisting of lowercase English letters, group them.
'''

from typing import List
class Solution:
    def GroupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            l = [0] * 26
            for c in s: # The list is modified only if the string is non-empty.
                l[ord(c) - ord("a")] += 1
            d.setdefault(tuple(l), []).append(s) # Neither a list nor a dictionary can serve as a dictionary key as they are mutable.
        return list(d.values()) # It returns a non-empty list of non-empty lists.

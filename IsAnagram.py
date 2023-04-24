'''
Given any two non-empty strings consisting, return True if the former is an anagram of the latter, and False otherwise.
'''

class Solution:
    def IsAnagram(self, s: str, t: str) -> bool: # It returns a Boolean object.
        if len(s) != len(t):
            return False
        sigma, tau = {}, {} # Imagine they are non-empty sets of ordered pairs.
        for i in range(len(s)): # range(-1, -10, 1) == range(2, 6, -2) for your information.
            sigma[s[i]] = 1 + sigma.get(s[i], 0)
            tau[t[i]] = 1 + sigma.get(t[i], 0)
        return sigma == tau # It returns True if they are subsets of each other.

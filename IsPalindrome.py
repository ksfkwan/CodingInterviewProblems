'''
A non-empty string is a palindrome if,
after converting all of its uppercase letters into lowercase letters
and removing all of its non-alphanumeric characters,
it is the same when you read it forwards from the beginning and backwards from the end.

The notion of symmetry plays a key role in this question.
'''

class Solution:
    def IsPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 # If l < r, there are at least two characters.
        while l < r:
            while l < r and not self.isalphanumeric(s[l]):
                l += 1
            # Either l < r or l == r after the above while loop.
            while l < r and not self.isalphanumeric(s[r]):
                r -= 1
            # If s[l] is alphanumeric, s[r] is alphanumeric.
            # Either l < r or l == r after the above two while loops.
            # If l < r, then both s[l] and s[r] are alphanumeric.
            if s[l].lower() != s[r].lower(): # The method also converts uppercase Greek letters into lowercase ones.
            # But what matters is the method returns one-character string if it is given one.
                return False
            l += 1
            r -= 1
        return True # A string with a length of one must be a palindrome.
    def isalphanumeric(self, c: str) -> bool: # Given an instance of the class and a one-character string, it returns a Boolean object.
        return (ord("0") <= ord(c) <= ord("9") # The ord() function converts a single Unicode character to its integer equivalent.
                or ord("A") <= ord(c) <= ord("Z")
                or ord("a") <= ord(c) <= ord("z")) # At most one of these three conditions can be met.

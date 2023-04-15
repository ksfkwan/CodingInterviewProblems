'''
You are given a non-empty string consisting only of uppercase letters and a non-negative integer less than or equal to the result of the string.
The algo shifts the current window if extending it does not increase the frequency.

Note that we are to return the longest length only and there is a difference between a valid length and a valid window.
'''

class Solution:
    def CharacterReplacement(self, s: str, k: int) -> int:
        # print(f's, k = {s}, {k}\n')
        dictionary = {}
        frequency = 0
        left = 0
        result = 0
        for right in range(len(s)):
            dictionary[s[right]] = 1 + dictionary.get(s[right], 0)
            frequency = max(frequency, dictionary[s[right]])
            

            if (right - left + 1) - frequency > k:
            # If (right - left + 1) - frequency <= k, there is a chance that the current substring can be changed into one consisting of letters of a kind, with no operations left.
                dictionary[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
            # print(f'left, right = {left}, {right}\ndictionary, frequency, result = {dictionary}, {frequency}, {result}\n')
        return result

Solution().CharacterReplacement('ADABACDAAAA', 2)

'''
You are given a non-empty string consisting only of uppercase letters and a non-negative integer less than or equal to the result of the string.
The algo may shift the current (non-empty) window if extending it does not increase the frequency.
Note that we are to return the longest length only and there is a difference between a valid length and a valid window. 
The number of occurences of the most frequent letter(s) in a valid substring plus k (>= 0) is greater than or equal to the length of the substring in question.
'''

class Solution:
    def CharacterReplacement(self, s: str, k: int) -> int:
        # print(f's, k = {s}, {k}\n')
        dictionary = {}
        frequency = 0
        left = 0
        result = 0
        for right in range(len(s)): # The first iteration is trivial, and the next letter if it exists is either one of the most frequent letters in the preceding window or not. 
            dictionary[s[right]] = 1 + dictionary.get(s[right], 0)
            frequency = max(frequency, dictionary[s[right]]) # frequency <= right - left + 1
            

            if (right - left + 1) - frequency > k:
            # If (right - left + 1) - frequency <= k, there is a chance that the current substring can be changed into one consisting of letters of a kind, with no operations left.
                dictionary[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
            # print(f'left, right = {left}, {right}\ndictionary, frequency, result = {dictionary}, {frequency}, {result}\n')
        return result

Solution().CharacterReplacement('ADABACDAAAA', 2)

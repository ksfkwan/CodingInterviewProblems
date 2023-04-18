'''
You are given a non-empty string consisting only of uppercase letters and a non-negative integer less than or equal to the result of the string. You can choose any character of the string and change it to any other uppercase character at most k times.
The algo may, depending on k, shift the current (non-empty) window if extending it does not increase the frequency.
Note that we are to return the longest length only.
A substring is valid if its length minus the number of occurences of its most frequent letter(s), i.e. the minimum number of operations it needs, is less than or equal to k.
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
            # Is it true that if the maximum number of occurences of a substring < frequency, its next extended substring if it exists is not valid?
            
            if (right - left + 1) - frequency > k:
            # If (right - left + 1) - frequency <= k, there is a chance that the current substring can be changed into one consisting of letters of a kind, with no operations left.
                dictionary[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
            # print(f'left, right = {left}, {right}\ndictionary, frequency, result = {dictionary}, {frequency}, {result}\n')
        return result

Solution().CharacterReplacement('ADABACDAAAA', 2)

'''
You are given a non-empty string consisting only of uppercase letters and a non-negative integer less than or equal to the result of the string.
The algo works becasue we are to return the longest possible length only.
There is a difference between a valid length and a valid window.
'''

class Solution:
    def CharacterReplacement(self, s: str, k: int) -> int:
        print(f's, k = {s}, {k}\n')
        dictionary = {}
        frequency = 0
        left = 0
        result = 0
        for right in range(len(s)):
            dictionary[s[right]] = 1 + dictionary.get(s[right], 0)
            frequency = max(frequency, dictionary[s[right]])

            if (right - left + 1) - frequency > k:
            # If (right - left + 1) - frequency <= k, there is a chance that the current substring can be changed to one consisting of letters of a kind.
                dictionary[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
            print(f'left, right = {left}, {right}\ndictionary, frequency, result = {dictionary}, {frequency}, {result}\n')
        return result  

Solution().CharacterReplacement('ADABACDCBBBA', 2)

'''
s, k = 'ABABBA', 2
s, k = ADABACDCBBBA, 2
'''

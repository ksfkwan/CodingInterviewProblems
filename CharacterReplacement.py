'''
You are given a non-empty string consisting only of uppercase letters and a non-negative integer less than or equal to the result of the string. You can choose any character of the string and change it to any other uppercase character at most k times. You have the right not to exhaust your power. 
The algo may, depending on k, shift the current (non-empty) window if extending it does not increase the maximum frequency. ('AB', 0) and ('AB', 1) are good examples.
A slower way would be examining every valid window. Note that we are to return the longest length only.
A substring is valid if its length minus the number of occurences of its most frequent letter(s), i.e. the minimum number of operations it needs, is less than or equal to k.
'''

class Solution:
    def CharacterReplacement(self, s: str, k: int) -> int:
        # print(f's, k = {s}, {k}\n')
        dictionary = {}
        mfrequency = 0
        left = 0
        result = 0
        for right in range(len(s)): # The right pointer is the protagonist and the first iteration is trivial.
            dictionary[s[right]] = 1 + dictionary.get(s[right], 0)
            mfrequency = max(mfrequency, dictionary[s[right]]) # right - left + 1 >= mfrequency since there are times when right - left + 1 is the only variable increasing.
            # Sometimes it reaches a point where right - left + 1 - mfrequency = k. This is when things get interesting.
            
            if (right - left + 1) - mfrequency > k:

                dictionary[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1) # This line of code is executed regardless.
            # print(f'left, right = {left}, {right}\ndictionary, mfrequency, result = {dictionary}, {mfrequency}, {result}\n')
        return result

'''
Try 'ADABACDAAAA'.
To have a better understanding of an algorithm in the future, you may want to think about how it is better than another one.
This algorithm initially searches for the first valid substring with a length of 1, then immediately the first valid substring with a length of 2 and so on.
The position of the last element of the first valid substring with a length of m + 1 if it exists must be greater than that of the last element of the first valid substring with a length of m.
If there is a valid window with a length of m + 1, then there is a valid window with a length of m.
The leftmost letter and the rightmost one are the most important and determine the maximum frequency of the next window. 
The new maximum frequency equals the frequency of the rightmost letter. 
'''

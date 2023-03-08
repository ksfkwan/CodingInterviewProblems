'''
The empty set is the subset of the empty set.
'''

def LengthOfLongestSubstring(string):
    characters = set()
    left = 0
    length = 0
    for right in range(len(string)):
        while string[right] in characters:
            characters.remove(string[left])
            left += 1
        characters.add(string[right])
        length = max(length, right - left + 1)
    return length

print(LengthOfLongestSubstring('abcabcbb'))

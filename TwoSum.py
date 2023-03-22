'''
Each interger array has a length of at least two and has exactly one solution.
And you may not use the same element twice.
If there are duplicated values, the algorithm will only look at the rightmost ones.
'''

class Solution:
    def TwoSum(self, integers, target):
        dictionary = {}
        for index, integer in enumerate(integers):
            complement = target - integer
            if complement in dictionary:
                return [dictionary[complement], index]
            dictionary[integer] = index

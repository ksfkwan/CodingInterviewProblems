'''
Given a non-empty integer array
and an positve integer k less than or equal to the number of unique elements in the array,
return the k most frequent elements.
It is guaranteed that the answer is unique.
'''

class Solution:
    def TopKFrequent(self, integers, k):
        dictionary = {}
        lists = [[] for i in range(0, len(integers) + 1, 1)]
        result = []
        for integer in integers:
            dictionary[integer] = 1 + dictionary.get(integer, 0)
        for key, value in dictionary.items():
            lists[value].append(key)
        for frequency in range(len(integers), 0, -1):
            for element in lists[frequency]:
                result.append(element)
                if len(result) == k:
                    return result

'''
The integer array has at least two elements and is sorted in non-decreasing order.
And there is exactly one solution.
Removing the last element in the input array, for example,
is equivalent to eliminating all the pairs associated with the element removed.
'''

class Solution:
    def TwoSum(self, integers, target):
        left, right = 0, len(integers) - 1
        while True:
            if integers[left] + integers[right] < target:
                left += 1
            elif integers[left] + integers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]

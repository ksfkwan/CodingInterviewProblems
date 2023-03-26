'''
heights[i] >= 0 and len(heights) >= 2.
Notice that we are only supposed to return the maximum amount.
Think algebraically.
'''

class Solution:
    def MaxArea(self, heights):
        '''
        :type heights: List[int]
        :rtype: int
        '''
        result = 0
        left, right = 0, len(heights) - 1
        while left < right:
            result = max(result, min(heights[left], heights[right]) * (right - left))
            if heights[left] <= heights[right]:
                left += 1 # \min(h_{0}, h_{n-1}), \ldots, \min(h_{n-2}, h_{n-1}) \leq \min(h_{0}, h_{n-1})
            elif heights[right] <= heights[left]:
                right -= 1
        return result

'''
The integer array has at least three elements.
Sorting a triplet in an unsorted array is like looking for its unique counterpart in the sorted array.
Next, our aim is to not produce duplicates.
'''

class Solution:
    def ThreeSum(self, integers):
        """
        :type integers: List[int]
        :rtype: List[List[int]]
        """
        integers.sort()
        result = []
        for index in range(len(integers)):
            if integers[index] > 0:
                break
            if index > 0 and integers[index] == integers[index - 1]:
                continue
            left, right = index + 1, len(integers) - 1
            while left < right:
                if integers[left] + integers[right] < 0 - integers[index]:
                    left += 1
                elif integers[left] + integers[right] > 0 - integers[index]:
                    right -= 1
                else:
                    result.append([integers[index], integers[left], integers[right]]) # After a triplet is appended, we try to incease the numeric value of its first element or that of its second.
                    left += 1 # The other pairs and the one we were just looking at are either duplicates or smaller than the target.
                    right -= 1 # The other pairs are either duplicates or greater than the target.
                    while integers[left] == integers[left - 1] and left < right:
                        left += 1 # The pairs are either duplicates or smaller than the target.
        return result

print(Solution().ThreeSum([-2, -2, -1, -1, 0, 0, 1, 1, 2, 2]))

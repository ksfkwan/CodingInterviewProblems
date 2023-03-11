'''
All the integers are unique and the non-empty list is sorted in ascending order.
10 ^ 4 - 1 > n \geq m \geq 0.
\lfloor (m + n) / 2 \rfloor = m + \lfloor (n - m) / 2 \rfloor if m and n are integers.
'''

class Solution:
    def Search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + ((right - left) // 2)
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

print(Solution().Search([-1, 0, 3, 5, 9, 12], 2))

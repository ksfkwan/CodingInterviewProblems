'''
Return only the maximum profit given a non-empty array of non-negative prices of a stock.
You can buy and sell the same stock on the same day.
It is possible that there is only one element in the array.
'''

class Solution:
    def MaxProfit(self, prices):
        '''
        :type prices: List[int]
        :rtype: int
        '''
        left = prices[0]
        result = 0
        for right in prices:
            if right < left:
                left = right
            # If p(n) < p(m), eliminate (p(m), p(n)), ..., (p(m), p(n + k)) only, where n + k + 1 = len(prices).
            # For any eliminated profit (a, b), there exists a profit (c, d) that has not been eliminated s.t. (a, b) <= (c, d).
            result = max(result, right - left)
        return result

print(Solution().MaxProfit([8, 9, 17, 17, 5, 19, 18, 6, 11, 5, 17, 15, 4, 13, 4, 3, 18, 19, 19, 6]))

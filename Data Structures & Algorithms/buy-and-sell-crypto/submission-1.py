class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 #buy
        R = 1 #sell
        maxP = 0
        while R < len(prices):
            #profitable
            if prices[L] < prices[R]:
                profit = prices[R] -prices[L]
                maxP = max(maxP , profit)
            else:
                L = R
            R += 1

        return maxP

            



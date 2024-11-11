class Solution(object):
    def maxProfit(self, prices):
        f1, f2, f3, f4 = -prices[0], 0, -prices[0], 0
        for i in range(1, len(prices)):
            f1 = max(f1, -prices[i])
            f2 = max(f2, f1 + prices[i])
            f3 = max(f3, f2 - prices[i])
            f4 = max(f4, f3 + prices[i])
        
        return f4

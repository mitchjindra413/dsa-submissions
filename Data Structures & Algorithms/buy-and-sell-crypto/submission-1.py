class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0

        for r in range(1, len(prices)):
            res = prices[r] - prices[l]
            if res < 0:
                l = r
            else:
                profit = max(profit, res) 
        
        return profit
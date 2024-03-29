class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit = 0
        low = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                profit = max(prices[i]-low, profit)
        return profit

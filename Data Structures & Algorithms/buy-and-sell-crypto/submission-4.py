class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            optimised_profit = max(prices[i+1:]) - prices[i]
            if optimised_profit > 0 and optimised_profit > max_profit:
                max_profit = optimised_profit
        return max_profit
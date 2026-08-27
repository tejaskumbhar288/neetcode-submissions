class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low = 0

        for i in range(len(prices)):
            if prices[i] < prices[low]:
                low = i

            profit = prices[i] - prices[low]
            max_profit = max(max_profit, profit)

        return max_profit
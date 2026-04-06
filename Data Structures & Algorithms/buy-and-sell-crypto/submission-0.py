class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        maxPrice = 0
        while end < len(prices):
            if prices[end] > prices[start]:
                profit = prices[end] - prices[start]
                maxPrice = max(maxPrice, profit)
            else:
                start = end   
            end += 1  
        return maxPrice
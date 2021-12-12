class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxPorfit = -1
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif maxPorfit < price - minPrice:
                maxPorfit = price - minPrice

        return maxPorfit
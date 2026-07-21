class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_res = 0
        min_price = prices[0]

        for price in prices[1:]:
            diff = price - min_price

            max_res = max(max_res, diff)
            min_price = min(min_price, price)

        return max_res    
            
        
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # prices=[7,1,5,3,6,4]. -> 5
         
        lowest = prices[0]
        profit = 0

        for price in prices[1:]:
            if price > lowest:
                profit = max(profit, price - lowest)
                print(profit)
            else:
                lowest = price

        return profit
    



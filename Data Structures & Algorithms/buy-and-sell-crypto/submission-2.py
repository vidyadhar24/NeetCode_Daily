class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # prices=[7,1,5,3,6,4]. -> 5

        # if the list is empty
        if not prices:
            return 0
         
        # We can achieve this in one single loop
        # as we traverse, maintain the loweest we have seen
        # if the current item is more than the lowest, check the profit
        # if this profit is more than the existing, keep this profit


        lowest = prices[0]
        profit = 0

        for price in prices:
            if price > lowest:
                profit = max(profit, price - lowest)
            else:
                lowest = price

        return profit
    



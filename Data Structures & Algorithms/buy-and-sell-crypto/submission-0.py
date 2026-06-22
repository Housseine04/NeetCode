class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        globalMin = float('inf')
        profit = 0
        for p in prices:
            if p < globalMin :
                globalMin = p
                continue
            if p - globalMin > profit:
                profit = p - globalMin

        return int(profit)
            

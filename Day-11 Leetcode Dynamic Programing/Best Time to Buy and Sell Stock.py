class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0 or prices==None:
            return 0
        
        profit = [0 for _ in range(len(prices))]
        min_stock = prices[0]
        for i in range(1, len(prices)):
            profit[i] = max(prices[i] - min_stock, profit[i-1])
            min_stock = min(prices[i], min_stock)
        return profit[len(prices)-1]
    

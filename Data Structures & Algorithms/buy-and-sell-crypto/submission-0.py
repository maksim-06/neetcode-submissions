class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        answ = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min_buy
            if profit > answ:
                answ = profit
            
            min_buy = min(min_buy, prices[i])
        return answ
        
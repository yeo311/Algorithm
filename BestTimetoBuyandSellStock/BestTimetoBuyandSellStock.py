# 121. Best Time to Buy and Sell Stock

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# List 를 시간당 주식 가격으로 생각하고, 사고 팔았을 때 가장 큰 이윤을 구하는 문제

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minValue = float('inf')
        for i in range(0, len(prices)):
            if prices[i] < minValue:
                minValue = prices[i]
            else:
                if profit < prices[i] - minValue:
                    profit = prices[i] - minValue
        
        return profit
    

if __name__ == "__main__":
    # Solution.maxProfit([1,2,3,4,5])
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
    
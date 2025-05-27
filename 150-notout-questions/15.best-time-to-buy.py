
# Buying and Selling Stocks Problem – Hard Level Problem
# You are given an array prices, where each element prices[i] represents the price of PrepCoin on the i-th day.

# Your task is to determine the maximum profit you can make by selecting one day to buy a PrepCoin and another day after it to sell.

# If it’s not possible to make any profit (e.g., prices are decreasing every day), you should return 0. This means you can also choose not to make any transactions.

# Example 1
# Input: prices = [10,1,5,6,7,1]
# Output: 6
# Explanation : Buy prices[1] and sell prices[4], profit = 7 – 1 = 6.

# Example 2
# Input: prices = [10,8,7,5,2]
# Output: 0
# Explanation : No profitable transactions can be made, thus the max profit is 0.

def maxProfit(prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
    
prices = [10,8,7,5,2]
print(maxProfit(prices))
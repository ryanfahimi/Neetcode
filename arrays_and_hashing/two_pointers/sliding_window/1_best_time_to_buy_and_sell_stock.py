from typing import List

# 121. Best Time to Buy and Sell Stock
# Easy

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Constraints:

# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4


class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_profit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            # Update the minimum price
            min_price = min(min_price, price)
            # Calculate the profit
            profit = price - min_price
            # Update the maximum profit
            max_profit = max(max_profit, profit)
        return max_profit

    def main(self):
        prices = [7, 1, 5, 3, 6, 4]
        print(f"Input: prices = {prices}")
        print(f"Output: {self.max_profit(prices)}")

        prices = [7, 6, 4, 3, 1]
        print(f"Input: prices = {prices}")
        print(f"Output: {self.max_profit(prices)}")


if __name__ == "__main__":
    Solution().main()

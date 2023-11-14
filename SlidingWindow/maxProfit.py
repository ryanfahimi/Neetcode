from typing import List


class maxProfit:
    def sliding_window(self, prices: List[int]) -> int:
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
        print(self.sliding_window(prices))


if __name__ == "__main__":
    maxProfit().main()

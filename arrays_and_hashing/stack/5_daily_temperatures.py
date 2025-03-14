from typing import List

# 739. Daily Temperatures
# Medium

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]


# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


class Solution:
    # Time: O(n)
    # Space: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the stack to store the indices of the temperatures
        stack = []
        # Initialize the result array with zeros
        result = [0] * len(temperatures)

        # Iterate through the temperatures
        for i, temperature in enumerate(temperatures):
            # While the stack is not empty and the current temperature is greater than the temperature at the top of the stack
            while stack and temperature > temperatures[stack[-1]]:
                # Update the result array with the difference in indices
                j = stack.pop()
                result[j] = i - j
            # Push the current index to the stack
            stack.append(i)

        return result

    def main(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        print(f"Input: temperatures = {temperatures}")
        print(f"Output: {self.dailyTemperatures(temperatures)}")

        temperatures = [30, 40, 50, 60]
        print(f"Input: temperatures = {temperatures}")
        print(f"Output: {self.dailyTemperatures(temperatures)}")

        temperatures = [30, 60, 90]
        print(f"Input: temperatures = {temperatures}")
        print(f"Output: {self.dailyTemperatures(temperatures)}")


if __name__ == "__main__":
    Solution().main()

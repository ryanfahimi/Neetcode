from typing import List

# 84. Largest Rectangle in Histogram
# Hard

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4


# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104


class LargestRectangleArea:
    # Time: O(n)
    # Space: O(n)
    def by_brute_force(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = [-1] * n  # Initialize left boundary array with -1

        # Fill left boundary array
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            stack.append(i)

        stack = []
        right = [n] * n  # Initialize right boundary array with n

        # Fill right boundary array
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]

            stack.append(i)

        max_area = 0
        # Calculate the maximum area
        for i in range(n):
            max_area = max(max_area, heights[i] * (right[i] - left[i] - 1))

        return max_area

    # Time: O(n)
    # Space: O(n)
    def by_optimal(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for current_index, current_height in enumerate(heights):
            start_index = current_index
            # Maintain the stack in increasing order of heights
            while stack and stack[-1][1] > current_height:
                popped_index, popped_height = stack.pop()
                # Calculate the area with the popped height as the smallest height
                max_area = max(max_area, popped_height * (current_index - popped_index))
                start_index = popped_index
            # Append the current bar with its starting index
            stack.append((start_index, current_height))

        # Calculate the area for the remaining bars in the stack
        for popped_index, popped_height in stack:
            max_area = max(max_area, popped_height * (len(heights) - popped_index))
        return max_area

    # Time: O(n)
    # Space: O(n)
    def by_one_pass(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i in range(n + 1):
            # If the current bar is lower than the bar at stack top, calculate the area
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                height = heights[stack.pop()]  # Height of the bar
                width = i if not stack else i - stack[-1] - 1  # Width of the rectangle
                max_area = max(max_area, height * width)  # Update max_area if needed
            stack.append(i)  # Push current index to stack

        return max_area

    def main(self):
        heights = [2, 1, 5, 6, 2, 3]
        print(f"Input: heights = {heights}")
        print(f"Brute Force Output: {self.by_brute_force(heights)}")
        print(f"Optimal Output: {self.by_optimal(heights)}")
        print(f"One Pass Output: {self.by_one_pass(heights)}")

        heights = [2, 4]
        print(f"Input: heights = {heights}")
        print(f"Brute Force Output: {self.by_brute_force(heights)}")
        print(f"Optimal Output: {self.by_optimal(heights)}")
        print(f"One Pass Output: {self.by_one_pass(heights)}")


if __name__ == "__main__":
    LargestRectangleArea().main()

from typing import List

# 11. Container With Most Water
# Medium

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:

# Input: height = [1,1]
# Output: 1


# Constraints:

# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4


class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_area(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            # Calculate the area
            area = min(height[left], height[right]) * (right - left)
            # Update the max area
            max_area = max(max_area, area)
            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

    def main(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        print(f"Input: height = {height}")
        print(f"Output: {self.max_area(height)}")

        height = [1, 1]
        print(f"Input: height = {height}")
        print(f"Output: {self.max_area(height)}")


if __name__ == "__main__":
    Solution().main()

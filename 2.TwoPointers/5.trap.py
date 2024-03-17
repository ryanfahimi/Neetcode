from typing import List

# 42. Trapping Rain Water
# Hard

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


# Constraints:

# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5


class Solution:
    # Time: O(n)
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        total = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                maxLeft = max(maxLeft, height[left])
                # Add the difference between the max height and the current height
                total += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                # Add the difference between the max height and the current height
                total += maxRight - height[right]
        return total

    def main(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        print(f"Input: height = {height}")
        print(f"Output: {self.trap(height)}")

        height = [4, 2, 0, 3, 2, 5]
        print(f"Input: height = {height}")
        print(f"Output: {self.trap(height)}")


if __name__ == "__main__":
    Solution().main()

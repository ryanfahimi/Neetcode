from typing import List

# 167. Two Sum II - Input Array Is Sorted
# Medium

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.


# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


# Constraints:

# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.


class Solution:
    # Time: O(n)
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at the start (left) and end (right) of the list
        left, right = 0, len(numbers) - 1

        # Continue until the two pointers meet
        while left < right:
            # Calculate the current sum of the elements at the left and right pointers
            curr_sum = numbers[left] + numbers[right]

            # If the current sum equals the target, return the indices of the two numbers
            if curr_sum == target:
                return [left + 1, right + 1]
            # If the current sum is less than the target, move the left pointer to the right
            elif curr_sum < target:
                left += 1
            # If the current sum is greater than the target, move the right pointer to the left
            else:
                right -= 1

        # If no two numbers sum to the target, return an empty list
        return []

    def main(self):
        numbers = [2, 7, 11, 15]
        target = 9
        print(f"Input: numbers = {numbers}, target = {target}")
        print(f"Output: {self.two_sum(numbers, target)}")

        numbers = [2, 3, 4]
        target = 6
        print(f"Input: numbers = {numbers}, target = {target}")
        print(f"Output: {self.two_sum(numbers, target)}")

        numbers = [-1, 0]
        target = -1
        print(f"Input: numbers = {numbers}, target = {target}")
        print(f"Output: {self.two_sum(numbers, target)}")


if __name__ == "__main__":
    Solution().main()

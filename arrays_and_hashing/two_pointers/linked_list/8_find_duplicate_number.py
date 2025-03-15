from typing import List

# 287. Find the Duplicate Number
# Medium

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.


# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3


# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.


# Follow up:


# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_duplicate(self, nums: List[int]) -> int:
        # Initialize the slow and fast pointers
        slow = nums[0]
        fast = nums[0]

        # Move the slow pointer by one step and the fast pointer by two steps
        slow = nums[slow]
        fast = nums[nums[fast]]

        # Find the intersection point of the two pointers
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Initialize the slow pointer to the start of the list
        slow = nums[0]

        # Move the slow pointer and the fast pointer by one step
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # Return the duplicate number
        return slow

    def main(self):
        nums = [1, 3, 4, 2, 2]
        print(f"Input: nums = {nums}")
        print(f"Output: {self.find_duplicate(nums)}")

        nums = [3, 1, 3, 4, 2]
        print(f"Input: nums = {nums}")
        print(f"Output: {self.find_duplicate(nums)}")

        nums = [3, 3, 3, 3, 3]
        print(f"Input: nums = {nums}")
        print(f"Output: {self.find_duplicate(nums)}")


if __name__ == "__main__":
    Solution().main()

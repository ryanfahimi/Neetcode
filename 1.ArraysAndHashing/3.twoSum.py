from typing import List

# 1. Two Sum
# Easy

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?


class twoSum:
    # Time: O(n^2)
    def brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # If the sum of the two numbers equals the target, return the indices of the two numbers
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # Time: O(n)
    def hash_table(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        for i, n in enumerate(nums):
            # If the complement is in the table, then we have found the pair
            complement = target - n
            if complement in sumMap:
                # Return the indices of the pair
                return [sumMap[complement], i]
            # Otherwise, add the number to the table
            sumMap[n] = i
        return []

    def main(self):
        nums = [2, 7, 11, 15]
        target = 9
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Brute Force Output: {self.brute_force(nums, target)}")
        print(f"Hash Table Output: {self.hash_table(nums, target)}")

        nums = [3, 2, 4]
        target = 6
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Brute Force Output: {self.brute_force(nums, target)}")
        print(f"Hash Table Output: {self.hash_table(nums, target)}")

        nums = [3, 3]
        target = 6
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Brute Force Output: {self.brute_force(nums, target)}")
        print(f"Hash Table Output: {self.hash_table(nums, target)}")


if __name__ == "__main__":
    twoSum().main()

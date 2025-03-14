from typing import List

# 15. 3Sum
# Medium

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# Constraints:

# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5


class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            # If the current number is the same as the previous number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:  # target == 0
                    result.append([nums[i], nums[left], nums[right]])
                    # If the next number is the same as the current number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # If the previous number is the same as the current number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move the pointers
                    left += 1
                    right -= 1
        return result

    def main(self):
        nums = [-1, 0, 1, 2, -1, -4]
        print(f"Input: nums = {nums}")
        print(f"Output: {self.three_sum(nums)}")

        nums = [0, 1, 1]
        print(f"Input: nums = {nums}")
        print(f"Output: {self.three_sum(nums)}")

        nums = [0, 0, 0]
        print(f"Input: nums = {nums}")
        print(f"Output: {self.three_sum(nums)}")


if __name__ == "__main__":
    Solution().main()

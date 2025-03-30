import heapq
from typing import List

# 215. Kth Largest Element in an Array
# Medium

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?


# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4


# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104


class Solution:
    # Time: O(n log k)
    # Space: O(k)
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def main(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        print(f"Input: nums = {nums}, k = {k}")
        print("Output:", self.find_kth_largest(nums, k))

        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        print(f"Input: nums = {nums}, k = {k}")
        print("Output:", self.find_kth_largest(nums, k))


if __name__ == "__main__":
    Solution().main()

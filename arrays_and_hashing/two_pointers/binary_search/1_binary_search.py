import bisect
from typing import List

# 704. Binary Search
# Easy

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.


class Search:
    # Time: O(logn)
    def by_recursive(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            # Base case: if the left index exceeds the right index, the target is not found
            if left > right:
                return -1

            # Calculate the middle index
            mid = left + (right - left) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid
            # If the middle element is less than the target, search in the right half
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            # If the middle element is greater than the target, search in the left half
            else:
                return binary_search(left, mid - 1)

        # Initiate the recursive binary search
        return binary_search(0, len(nums) - 1)

    # Time: O(logn)
    def by_iterative(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Continue searching while the left index is less than or equal to the right index
        while left <= right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid
            # If the middle element is less than the target, search in the right half
            elif nums[mid] < target:
                left = mid + 1
            # If the middle element is greater than the target, search in the left half
            else:
                right = mid - 1

        # If the target is not found, return -1
        return -1

    # Time: O(logn)
    def by_upper_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        # Continue searching while the left index is less than the right index
        while left < right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            # If the middle element is less than or equal to the target, search in the right half
            if nums[mid] <= target:
                left = mid + 1
            # If the middle element is greater than the target, search in the left half
            else:
                right = mid

        # Check if the element just before the left index is the target
        return left - 1 if left > 0 and nums[left - 1] == target else -1

    # Time: O(logn)
    def by_lower_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        # Continue searching while the left index is less than the right index
        while left < right:
            # Calculate the middle index
            mid = left + (right - left) // 2

            # If the middle element is less than the target, search in the right half
            if nums[mid] < target:
                left = mid + 1
            # If the middle element is greater than or equal to the target, search in the left half
            else:
                right = mid

        # Check if the left index is within bounds and the element at the left index is the target
        return left if left < len(nums) and nums[left] == target else -1

    # Time: O(logn)
    def by_built_in_function(self, nums: List[int], target: int) -> int:
        # Use bisect_left to find the insertion point for target in nums
        index = bisect.bisect_left(nums, target)

        # Check if the target is found at the insertion point
        return index if index < len(nums) and nums[index] == target else -1

    def main(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        print(f"Input: nums = {nums}, target = {target}")
        print("Output (Recursive):", self.by_recursive(nums, target))
        print("Output (Iterative):", self.by_iterative(nums, target))
        print("Output (Upper Bound):", self.by_upper_bound(nums, target))
        print("Output (Lower Bound):", self.by_lower_bound(nums, target))
        print("Output (Built-in Function):", self.by_built_in_function(nums, target))

        target = 2
        print(f"\nInput: nums = {nums}, target = {target}")
        print("Output (Recursive):", self.by_recursive(nums, target))
        print("Output (Iterative):", self.by_iterative(nums, target))
        print("Output (Upper Bound):", self.by_upper_bound(nums, target))
        print("Output (Lower Bound):", self.by_lower_bound(nums, target))
        print("Output (Built-in Function):", self.by_built_in_function(nums, target))


if __name__ == "__main__":
    Search().main()

from typing import List

# 33. Search in Rotated Sorted Array
# Medium

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1


# Constraints:


# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104
class Search:
    # Time: O(logn)
    def by_two_passes(self, nums: List[int], target: int) -> int:
        # Initialize pointers
        left, right = 0, len(nums) - 1

        # Find the index of the smallest value using binary search.
        # Loop until left meets right
        while left < right:
            mid = left + (right - left) // 2
            # If mid element is greater than the rightmost element, the smallest value is to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # The smallest value's index is the pivot
        pivot = left
        # Reset pointers for the second binary search
        left, right = 0, len(nums) - 1

        # Perform binary search considering the pivot
        while left <= right:
            mid = left + (right - left) // 2
            # Adjust mid index with pivot
            mid_val = nums[(mid + pivot) % len(nums)]

            # Standard binary search logic
            if mid_val < target:
                left = mid + 1
            elif mid_val > target:
                right = mid - 1
            else:
                return (mid + pivot) % len(nums)

        # If target is not found, return -1
        return -1

    # Time: O(logn)
    def by_one_pass(self, nums: List[int], target: int) -> int:
        # Initialize pointers
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2
            # Check if mid element is the target
            if nums[mid] == target:
                return mid
            # Determine if the left half is sorted
            elif nums[left] <= nums[mid]:
                # Check if target is within the left half
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, the right half must be sorted
            else:
                # Check if target is within the right half
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # If target is not found, return -1
        return -1

    def main(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output (Two Passes): {self.by_two_passes(nums, target)}")
        print(f"Output (One Pass): {self.by_one_pass(nums, target)}")

        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output (Two Passes): {self.by_two_passes(nums, target)}")
        print(f"Output (One Pass): {self.by_one_pass(nums, target)}")

        nums = [1]
        target = 0
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output (Two Passes): {self.by_two_passes(nums, target)}")
        print(f"Output (One Pass): {self.by_one_pass(nums, target)}")


if __name__ == "__main__":
    Search().main()

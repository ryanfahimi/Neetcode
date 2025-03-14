from typing import List

# 153. Find Minimum in Rotated Sorted Array
# Medium

# Hint
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.


# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.


class FindMin:
    # Time: O(log n)
    # Space: O(1)
    def by_iterative(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minimum = nums[0]

        while left <= right:
            # If the subarray is already sorted, the minimum is the leftmost element
            if nums[left] < nums[right]:
                minimum = min(minimum, nums[left])
                break

            mid = left + (right - left) // 2
            minimum = min(minimum, nums[mid])

            # If we are in the left sorted portion, move to the right sorted portion
            if nums[mid] >= nums[left]:
                left = mid + 1
            # If we are in the right sorted portion, move to the left sorted portion
            else:
                right = mid - 1

        return minimum

    # Time: O(log n)
    # Space: O(1)
    def by_lower_bound(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # If mid element is less than the rightmost element, the minimum is in the left part
            if nums[mid] < nums[right]:
                right = mid
            # If mid element is greater than or equal to the rightmost element, the minimum is in the right part
            else:
                left = mid + 1

        # After the loop, left will point to the minimum element
        return nums[left]

    def main(self):
        nums = [3, 4, 5, 1, 2]
        print(f"Input: nums = {nums}")
        print("Output (Iterative):", self.by_iterative(nums))
        print("Output (Lower Bound):", self.by_lower_bound(nums))

        nums = [4, 5, 6, 7, 0, 1, 2]
        print(f"\nInput: nums = {nums}")
        print("Output (Iterative):", self.by_iterative(nums))
        print("Output (Lower Bound):", self.by_lower_bound(nums))

        nums = [11, 13, 15, 17]
        print(f"\nInput: nums = {nums}")
        print("Output (Iterative):", self.by_iterative(nums))
        print("Output (Lower Bound):", self.by_lower_bound(nums))


if __name__ == "__main__":
    FindMin().main()

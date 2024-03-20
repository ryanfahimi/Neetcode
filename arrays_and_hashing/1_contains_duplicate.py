from typing import List

# 217. Contains Duplicate
# Easy

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# Constraints:

# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9


class ContainsDuplicate:
    # Time: O(nlogn)
    def by_sorting(self, nums: List[int]) -> bool:
        # Sort the numbers
        nums.sort()
        for i in range(1, len(nums)):
            # If the current number is the same as the previous number
            if nums[i] == nums[i - 1]:
                return True
        return False

    # Time: O(n)
    def by_hash_set(self, nums: List[int]) -> bool:
        # Create a set to store the numbers seen so far
        seen = set()
        for num in nums:
            # If the number is already in the set, return True
            if num in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(num)
        # If we have gone through all the numbers without finding a duplicate, return False
        return False

    def main(self):
        nums = [1, 2, 3, 1]
        print(f"Input: nums = {nums}")
        print(f"Sorting Output: {self.by_sorting(nums)}")
        print(f"Hash Set Output: {self.by_hash_set(nums)}")

        nums = [1, 2, 3, 4]
        print(f"Input: nums = {nums}")
        print(f"Sorting Output: {self.by_sorting(nums)}")
        print(f"Hash Set Output: {self.by_hash_set(nums)}")

        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        print(f"Input: nums = {nums}")
        print(f"Sorted Output: {self.by_sorting(nums)}")
        print(f"Hash Set Output: {self.by_hash_set(nums)}")


if __name__ == "__main__":
    ContainsDuplicate().main()

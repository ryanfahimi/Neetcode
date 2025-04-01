from typing import List

# 90. Subsets II
# Medium

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


# Constraints:


# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
class SubsetsWithDup:
    # Time: O(2^n * n)
    # Space: O(n)
    def by_backtracking(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result list and the current subset
        subsets = []
        subset = []

        def backtrack(index: int):
            # If we have considered all elements, add the current subset to the result
            if index == len(nums):
                subsets.append(subset.copy())
                return

            # Include the current element in the subset
            subset.append(nums[index])
            backtrack(index + 1)

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            # Backtrack by excluding the current element from the subset
            subset.pop()
            backtrack(index + 1)

        nums.sort()  # Sort the array to handle duplicates
        backtrack(0)
        return subsets

    # Time: O(2^n * n)
    # Space: O(n)
    def by_optimal(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result list and the current subset
        subsets = []
        subset = []

        def backtrack(start: int):
            # Add the current subset to the result
            subsets.append(subset.copy())

            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Include the current element in the subset
                subset.append(nums[i])
                backtrack(i + 1)
                # Backtrack by excluding the current element from the subset
                subset.pop()

        nums.sort()  # Sort the array to handle duplicates
        backtrack(0)
        return subsets

    def main(self):
        nums = [1, 2, 2]
        print(f"Input: {nums}")
        print(f"Output (Backtracking): {self.by_backtracking(nums)}")
        print(f"Output (Optimal): {self.by_optimal(nums)}")

        nums = [0]
        print(f"Input: {nums}")
        print(f"Output (Backtracking): {self.by_backtracking(nums)}")
        print(f"Output (Optimal): {self.by_optimal(nums)}")


if __name__ == "__main__":
    SubsetsWithDup().main()

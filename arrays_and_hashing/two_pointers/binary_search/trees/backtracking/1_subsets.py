from typing import List

# 78. Subsets
# Medium

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


# Constraints:


# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
class Subsets:
    # Time: O(2^n * n)
    # Space: O(n)
    def by_backtracking(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result list and the current subset
        result = []
        subset = []

        def backtrack(index: int):
            # If we have considered all elements, add the current subset to the result
            if index == len(nums):
                result.append(subset.copy())
                return

            # Include the current element in the subset
            subset.append(nums[index])
            backtrack(index + 1)

            # Backtrack by excluding the current element from the subset
            subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return result

    # Time: O(2^n * n)
    # Space: O(n)
    def by_optimal(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result list and the current subset
        result = []
        subset = []

        def backtrack(start: int):
            # Add the current subset to the result
            result.append(subset.copy())

            for i in range(start, len(nums)):
                # Include the current element in the subset
                subset.append(nums[i])
                backtrack(i + 1)
                # Backtrack by excluding the current element from the subset
                subset.pop()

        backtrack(0)
        return result

    def main(self):
        nums = [1, 2, 3]
        print(f"Input: {nums}")
        print(f"Output (Backtracking): {self.by_backtracking(nums)}")
        print(f"Output (Optimal): {self.by_optimal(nums)}")

        nums = [0]
        print(f"Input: {nums}")
        print(f"Output (Backtracking): {self.by_backtracking(nums)}")
        print(f"Output (Optimal): {self.by_optimal(nums)}")


if __name__ == "__main__":
    Subsets().main()

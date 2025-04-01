from typing import List

# 46. Permutations
# Medium

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]


# Constraints:


# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
class Permute:
    # Time: O(n * n!)
    # Space: O(n)
    def by_backtracking(self, nums: List[int]) -> List[List[int]]:
        # List to store all valid permutations
        permutations = []
        # Temporary list to store the current permutation
        permutation = []

        # Helper function to perform backtracking
        def backtrack(picked: List[bool]):
            # If the current permutation is of the same length as nums, add it to the result
            if len(permutation) == len(nums):
                permutations.append(permutation.copy())
                return

            for i, num in enumerate(nums):
                if picked[i]:
                    continue
                # Include the current number in the permutation
                permutation.append(num)
                picked[i] = True  # Mark the number as used

                backtrack(picked)  # Recur to fill the next position
                permutation.pop()
                picked[i] = False  # Backtrack by unmarking the number

        # Initialize a list to track used numbers
        used = [False] * len(nums)
        backtrack(used)
        return permutations

    # Time: O(n * n!)
    # Space: O(n)
    def by_optimal(self, nums: List[int]) -> List[List[int]]:
        # List to store all valid permutations
        permutations = []

        # Helper function to perform backtracking
        def backtrack(start: int):
            # If we have fixed all positions, add the current permutation to the result
            if start == len(nums) - 1:
                permutations.append(nums.copy())
                return

            # Iterate through the array and swap elements to generate permutations
            for i in range(start, len(nums)):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recur to fix the next position
                backtrack(start + 1)
                # Backtrack by swapping the elements back to their original positions
                nums[start], nums[i] = nums[i], nums[start]

        # Start the backtracking process from the first index
        backtrack(0)
        return permutations

    def main(self):
        nums = [1, 2, 3]
        print(f"Input: {nums}")
        print(f"Output (Backtracking): {self.by_backtracking(nums)}")
        print(f"Output (Optimal): {self.by_optimal(nums)}")

        nums = [0, 1]
        print(f"Input: {nums}")
        print(f"Output (Backtracking): {self.by_backtracking(nums)}")
        print(f"Output (Optimal): {self.by_optimal(nums)}")

        nums = [1]
        print(f"Input: {nums}")
        print(f"Output (Backtracking): {self.by_backtracking(nums)}")
        print(f"Output (Optimal): {self.by_optimal(nums)}")


if __name__ == "__main__":
    Permute().main()

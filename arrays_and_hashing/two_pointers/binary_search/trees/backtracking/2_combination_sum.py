from typing import List

# 39. Combination Sum
# Medium

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []


# Constraints:


# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
class CombinationSum:
    # Time: O(2^(t/m))
    # Space: O(t/m)
    def by_backtracking(self, candidates: List[int], target: int) -> List[List[int]]:
        # List to store all valid combinations
        combinations = []
        # Temporary list to store the current combination
        combination = []

        # Helper function to perform backtracking
        def backtrack(index: int, total: int):
            # If the current sum equals the target, add the combination to the result
            if total == target:
                combinations.append(combination.copy())
                return
            # If the current sum exceeds the target or we have considered all candidates, stop exploring this path
            if total > target or index == len(candidates):
                return

            combination.append(candidates[index])  # Include the current candidate
            # Recur with the same index (allowing reuse of the same number)
            backtrack(index, total + candidates[index])
            combination.pop()  # Backtrack by removing the last added candidate
            backtrack(index + 1, total)  # Explore the next candidate

        # Start backtracking from index 0 with an initial sum of 0
        backtrack(0, 0)
        return combinations

    # Time: O(2^(t/m))
    # Space: O(t/m)
    def by_optimal(self, candidates: List[int], target: int) -> List[List[int]]:
        # List to store all valid combinations
        combinations = []
        # Temporary list to store the current combination
        combination = []

        # Helper function to perform backtracking
        def backtrack(start: int, total: int):
            # If the current sum equals the target, add the combination to the result
            if total == target:
                combinations.append(combination.copy())
                return
            # If the current sum exceeds the target, stop exploring this path
            if total > target:
                return

            # Iterate through the candidates starting from the current index
            for i in range(start, len(candidates)):
                # Add the current candidate to the combination
                combination.append(candidates[i])
                # Recursively call backtrack with the updated sum and the same index (allowing reuse of the same number)
                backtrack(i, total + candidates[i])
                # Remove the last added candidate to backtrack and explore other possibilities
                combination.pop()

        # Start backtracking from index 0 with an initial sum of 0
        backtrack(0, 0)
        return combinations

    def main(self):
        candidates = [2, 3, 6, 7]
        target = 7
        print(f"Input: {candidates}, {target}")
        print(f"Output (Backtracking): {self.by_backtracking(candidates, target)}")
        print(f"Output (Optimal): {self.by_optimal(candidates, target)}")

        candidates = [2, 3, 5]
        target = 8
        print(f"Input: {candidates}, {target}")
        print(f"Output (Backtracking): {self.by_backtracking(candidates, target)}")
        print(f"Output (Optimal): {self.by_optimal(candidates, target)}")

        candidates = [2]
        target = 1
        print(f"Input: {candidates}, {target}")
        print(f"Output (Backtracking): {self.by_backtracking(candidates, target)}")
        print(f"Output (Optimal): {self.by_optimal(candidates, target)}")


if __name__ == "__main__":
    CombinationSum().main()

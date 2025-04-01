from collections import Counter
from typing import List

# 40. Combination Sum II
# Medium

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.


# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]


# Constraints:


# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
class CombinationSum2:
    # Time: O(n * 2^n)
    # Space: O(n)
    def by_backtracking(self, candidates: List[int], target: int) -> List[List[int]]:
        # List to store all valid combinations
        combinations = []
        # Temporary list to store the current combination
        combination = []

        # Sort the candidates to handle duplicates and facilitate backtracking
        candidates.sort()

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
            backtrack(index + 1, total + candidates[index])
            combination.pop()  # Backtrack by removing the last added candidate
            # Skip duplicates to avoid duplicate combinations
            while (
                index + 1 < len(candidates)
                and candidates[index] == candidates[index + 1]
            ):
                index += 1
            backtrack(index + 1, total)  # Explore the next candidate

        # Start backtracking from index 0 with an initial sum of 0
        backtrack(0, 0)
        return combinations

    # Time: O(n * 2^n)
    # Space: O(n)
    def by_hash_map(self, candidates: List[int], target: int) -> List[List[int]]:
        # List to store all valid combinations
        combinations = []
        # Temporary list to store the current combination
        combination = []
        # Counter to count occurrences of each candidate
        counter = Counter(candidates)
        # List to store unique candidates
        unique_candidates = list(counter.keys())

        # Helper function to perform backtracking
        def backtrack(index: int, total: int):
            # If the current sum equals the target, add the combination to the result
            if total == target:
                combinations.append(combination.copy())
                return
            # If the current sum exceeds the target or we have considered all candidates, stop exploring this path
            if total > target or index == len(unique_candidates):
                return

            current_candidate = unique_candidates[index]
            # If the current candidate can still be used
            if counter[current_candidate] > 0:
                # Include the current candidate in the combination
                combination.append(current_candidate)
                # Decrease its count in the counter
                counter[current_candidate] -= 1
                # Recur with the same index and updated total
                backtrack(index, total + current_candidate)
                # Backtrack by restoring the count and removing the candidate
                counter[current_candidate] += 1
                combination.pop()

            # Skip the current candidate and move to the next one
            backtrack(index + 1, total)

        # Start backtracking from index 0 with an initial sum of 0
        backtrack(0, 0)
        return combinations

    # Time: O(n * 2^n)
    # Space: O(n)
    def by_optimal(self, candidates: List[int], target: int) -> List[List[int]]:
        # List to store all valid combinations
        combinations = []
        # Temporary list to store the current combination
        combination = []

        # Sort the candidates to handle duplicates and facilitate backtracking
        candidates.sort()

        # Helper function to perform backtracking
        def backtrack(start: int, total: int):
            # If the current sum equals the target, add the combination to the result
            if total == target:
                combinations.append(combination.copy())
                return
            # If the current sum exceeds the target, stop exploring this path
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                combination.append(candidates[i])
                # Recur with the next index and updated total
                backtrack(i + 1, total + candidates[i])
                combination.pop()  # Backtrack by removing the last added candidate

        # Start backtracking from index 0 with an initial sum of 0
        backtrack(0, 0)
        return combinations

    def main(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        print(f"Input: {candidates}, Target: {target}")
        print(f"Output (Backtracking): {self.by_backtracking(candidates, target)}")
        print(f"Output (Hash Map): {self.by_hash_map(candidates, target)}")
        print(f"Output (Optimal): {self.by_optimal(candidates, target)}")

        candidates = [2, 5, 2, 1, 2]
        target = 5
        print(f"Input: {candidates}, Target: {target}")
        print(f"Output (Backtracking): {self.by_backtracking(candidates, target)}")
        print(f"Output (Hash Map): {self.by_hash_map(candidates, target)}")
        print(f"Output (Optimal): {self.by_optimal(candidates, target)}")


if __name__ == "__main__":
    CombinationSum2().main()

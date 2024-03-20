from typing import List

# 128. Longest Consecutive Sequence
# Medium

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# Constraints:

# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9


class LongestConsecutive:
    # Time: O(n)
    def by_set(self, nums: List[int]) -> int:
        # Create a set of the numbers
        num_set = set(nums)
        longest_streak = 0
        # Iterate through the set
        for num in num_set:
            # If the previous number is not in the set
            if num - 1 not in num_set:
                current_streak = 1
                # While the next number is in the set
                while num + current_streak in num_set:
                    # Increment the current number and the current streak
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)
        return longest_streak

    # Time: O(n)
    def by_hash_map(self, nums: List[int]) -> int:
        # Initialize a hash map to store the streak length for each number
        streaks = {}
        # Initialize a variable to store the length of the longest streak
        longest_streak = 0

        # Iterate over each number in the list
        for num in nums:
            # If the number is not already in the hash map
            if num not in streaks:
                # Get the length of the streak to the left and right of the current number
                left = streaks.get(num - 1, 0)
                right = streaks.get(num + 1, 0)

                # Calculate the current streak by adding the lengths of the streaks to the left and right of the current number
                current_streak = left + right + 1

                # Update the longest streak if the current streak is longer
                longest_streak = max(longest_streak, current_streak)

                # Update the streaks of the numbers to the left and right of the current number
                streaks[num] = current_streak
                streaks[num - left] = current_streak
                streaks[num + right] = current_streak

        # Return the length of the longest streak
        return longest_streak

    def main(self):
        nums = [100, 4, 200, 1, 3, 2]
        print(f"Input: nums = {nums}")
        print(f"Set Output: {self.by_set(nums)}")
        print(f"Hash Map Output: {self.by_hash_map(nums)}")

        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        print(f"Input: nums = {nums}")
        print(f"Set Output: {self.by_set(nums)}")
        print(f"Hash Map Output: {self.by_hash_map(nums)}")


if __name__ == "__main__":
    LongestConsecutive().main()

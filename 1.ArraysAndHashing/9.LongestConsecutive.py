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
    def hashSet(self, nums: List[int]) -> int:
        # Create a set of the numbers
        numSet = set(nums)
        longestStreak = 0
        # Iterate through the set
        for num in numSet:
            # If the previous number is not in the set
            if num - 1 not in numSet:
                currentStreak = 1
                # While the next number is in the set
                while num + currentStreak in numSet:
                    # Increment the current number and the current streak
                    currentStreak += 1

                longestStreak = max(longestStreak, currentStreak)
        return longestStreak

    # Time: O(n)
    def hashTable(self, nums: List[int]) -> int:
        # Initialize a dictionary to store the streak length for each number
        numDict = {}
        # Initialize a variable to store the length of the longest streak
        longestStreak = 0

        # Iterate over each number in the list
        for num in nums:
            # If the number is not already in the dictionary
            if num not in numDict:
                # Get the length of the streak to the left and right of the current number
                left = numDict.get(num - 1, 0)
                right = numDict.get(num + 1, 0)

                # Calculate the current streak by adding the lengths of the streaks to the left and right of the current number
                currentStreak = left + right + 1

                # Update the longest streak if the current streak is longer
                longestStreak = max(longestStreak, currentStreak)

                # Update the streaks of the numbers to the left and right of the current number
                numDict[num] = currentStreak
                numDict[num - left] = currentStreak
                numDict[num + right] = currentStreak

        # Return the length of the longest streak
        return longestStreak

    def main(self):
        nums = [100, 4, 200, 1, 3, 2]
        print(f"Input: nums = {nums}")
        print(f"Hash Set Output: {self.hashSet(nums)}")
        print(f"Hash Table Output: {self.hashTable(nums)}")

        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        print(f"Input: nums = {nums}")
        print(f"Hash Set Output: {self.hashSet(nums)}")
        print(f"Hash Table Output: {self.hashTable(nums)}")


if __name__ == "__main__":
    LongestConsecutive().main()

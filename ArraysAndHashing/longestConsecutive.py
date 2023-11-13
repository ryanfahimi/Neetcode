from typing import List
import timeit


class longestConsecutive:
    # Time: O(n)
    def hash_set(self, nums: List[int]) -> int:
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
    def hash_table(self, nums: List[int]) -> int:
        num_dict = {}
        longest_streak = 0
        for num in nums:
            if num not in num_dict:
                # Get the length of the streak to the left and right of the current number
                left = num_dict.get(num - 1, 0)
                right = num_dict.get(num + 1, 0)
                # Calculate the current streak
                current_streak = left + right + 1
                longest_streak = max(longest_streak, current_streak)
                # Update the streaks of the numbers to the left and right of the current number
                num_dict[num] = current_streak
                num_dict[num - left] = current_streak
                num_dict[num + right] = current_streak
        return longest_streak

    def main(self):
        nums = [100, 4, 200, 1, 3, 2]
        funcs = [self.hash_set, self.hash_table]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(nums))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    longestConsecutive().main()

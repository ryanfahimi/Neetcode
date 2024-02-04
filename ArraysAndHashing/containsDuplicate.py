from typing import List
import timeit


class containsDuplicate:
    # Time: O(nlogn)
    # Space: O(1)
    def sorted(self, nums: List[int]) -> bool:
        # Sort the numbers
        nums.sort()
        for i in range(1, len(nums)):
            # If the current number is the same as the previous number
            if nums[i] == nums[i - 1]:
                return True
        return False

    # Time: O(n)
    # Space: O(n)
    def hash_set(self, nums: List[int]) -> bool:
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
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
        funcs = [self.sorted, self.hash_set]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(nums))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    containsDuplicate().main()

from typing import List
import timeit


class containsDuplicate:
    # Time: O(n^2)
    def brute_force(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

    # Time: O(nlogn)
    def sorted(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            # If the current number is the same as the previous number
            if nums[i] == nums[i - 1]:
                return True
        return False

    # Time: O(n)
    def hash_set(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def main(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
        funcs = [self.brute_force, self.sorted, self.hash_set]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(nums))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    containsDuplicate().main()

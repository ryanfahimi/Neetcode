import timeit
from typing import List


class twoSum:
    # Time: O(n^2)
    def brute_force(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # Time: O(n)
    def hash_table(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        for i, n in enumerate(nums):
            # If the complement is in the map, then we have found the pair
            complement = target - n
            if complement in sumMap:
                return [sumMap[complement], i]
            sumMap[n] = i
        return []

    def main(self):
        nums = [2, 7, 11, 15]
        target = 9
        funcs = [self.brute_force, self.hash_table]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(nums, target))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    twoSum().main()

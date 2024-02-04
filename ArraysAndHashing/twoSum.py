from typing import List


class twoSum:
    # Time: O(n)
    # Space: O(n)
    def hash_table(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        for i, n in enumerate(nums):
            # If the complement is in the table, then we have found the pair
            complement = target - n
            if complement in sumMap:
                # Return the indices of the pair
                return [sumMap[complement], i]
            # Otherwise, add the number to the table
            sumMap[n] = i
        return []

    def main(self):
        nums = [2, 7, 11, 15]
        target = 9
        print(self.hash_table(nums, target))


if __name__ == "__main__":
    twoSum().main()

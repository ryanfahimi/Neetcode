from math import ceil
from typing import List

# 875. Koko Eating Bananas
# Medium

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23


# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109


class MinEatingSpeed:
    # Time: O(nlogn)
    def by_lower_bound(self, piles: List[int], h: int) -> int:
        # Initialize the binary search bounds
        left, right = 1, max(piles)

        # Perform binary search to find the minimum eating speed
        while left < right:
            mid = left + (right - left) // 2
            hours = sum(ceil(pile / mid) for pile in piles)

            # If the hours exceed the limit, search in the right half
            if hours > h:
                left = mid + 1
            # If the hours are within the limit, search in the left half
            else:
                right = mid

        return left

    # Time: O(nlogn)
    def by_recursive(self, piles: List[int], h: int) -> int:
        def binary_search(left, right):
            # Base case: if the search bounds converge, return the left bound
            if left == right:
                return left

            # Calculate the middle point
            mid = left + (right - left) // 2
            # Calculate the total hours needed to eat all bananas at speed mid
            hours = sum(ceil(pile / mid) for pile in piles)

            # If the hours exceed the limit, search in the right half
            if hours > h:
                return binary_search(mid + 1, right)
            # If the hours are within the limit, search in the left half
            else:
                return binary_search(left, mid)

        # Start the binary search with the initial bounds
        return binary_search(1, max(piles))

    def main(self):
        piles = [3, 6, 7, 11]
        h = 8
        print(f"Input: piles = {piles}, h = {h}")
        print("Output (Lower Bound):", self.by_lower_bound(piles, h))
        print("Output (Recursive):", self.by_recursive(piles, h))

        piles = [30, 11, 23, 4, 20]
        h = 5
        print(f"\nInput: piles = {piles}, h = {h}")
        print("Output (Lower Bound):", self.by_lower_bound(piles, h))
        print("Output (Recursive):", self.by_recursive(piles, h))

        h = 6
        print(f"\nInput: piles = {piles}, h = {h}")
        print("Output (Lower Bound):", self.by_lower_bound(piles, h))
        print("Output (Recursive):", self.by_recursive(piles, h))


if __name__ == "__main__":
    MinEatingSpeed().main()

import heapq
from typing import List

# 1046. Last Stone Weight
# Easy

# Hint
# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.


# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:

# Input: stones = [1]
# Output: 1


# Constraints:


# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert stones to a max-heap by negating the values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Extract the two heaviest stones
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            # If they are not equal, push the difference back into the heap
            if first != second:
                heapq.heappush(max_heap, first - second)

        # If there is a stone left, return its weight, otherwise return 0
        return -max_heap[0] if max_heap else 0

    def main(self):
        stones = [2, 7, 4, 1, 8, 1]
        print(f"Input: stones = {stones}")
        print(f"Output: {self.lastStoneWeight(stones)}")

        stones = [1]
        print(f"Input: stones = {stones}")
        print(f"Output: {self.lastStoneWeight(stones)}")


if __name__ == "__main__":
    Solution().main()

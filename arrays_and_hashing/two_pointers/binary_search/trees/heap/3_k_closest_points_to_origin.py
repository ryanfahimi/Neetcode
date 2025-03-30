import heapq
from math import sqrt
from typing import List

# 973. K Closest Points to Origin
# Medium

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


# Example 1:


# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.


# Constraints:


# 1 <= k <= points.length <= 104
# -104 <= xi, yi <= 104
class KClosest:
    # Time: O(n log n)
    # Space: O(n)
    def by_min_heap(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a min-heap based on the distance from the origin
        min_heap = [(sqrt(x**2 + y**2), [x, y]) for x, y in points]
        heapq.heapify(min_heap)

        # Extract the k closest points from the heap
        return [heapq.heappop(min_heap)[1] for _ in range(k)]

    # Time: O(n log k)
    # Space: O(k)
    def by_max_heap(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a max-heap based on the distance from the origin
        max_heap = []
        for x, y in points:
            distance = sqrt(x**2 + y**2)
            # Push the negative distance to create a max-heap
            heapq.heappush(max_heap, (-distance, [x, y]))
            # If the heap exceeds size k, pop the farthest point
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        # Extract the k closest points from the heap and return them in the original order
        return [point for _, point in max_heap]

    def main(self):
        points = [[1, 3], [-2, 2]]
        k = 1
        print(f"Input: points = {points}, k = {k}")
        print(f"Output (Min Heap): {self.by_min_heap(points, k)}")
        print(f"Output (Max Heap): {self.by_max_heap(points, k)}")

        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        print(f"Input: points = {points}, k = {k}")
        print(f"Output (Min Heap): {self.by_min_heap(points, k)}")
        print(f"Output (Max Heap): {self.by_max_heap(points, k)}")


if __name__ == "__main__":
    KClosest().main()

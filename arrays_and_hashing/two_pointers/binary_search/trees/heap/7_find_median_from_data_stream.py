import heapq

# 295. Find Median from Data Stream
# Hard

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0


# Constraints:

# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.


# Follow up:


# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
class MedianFinder:

    def __init__(self):
        # Initialize two heaps: max_heap for the left half (negative values for max-heap behavior)
        # and min_heap for the right half (default min-heap behavior).
        self.max_heap = []
        self.min_heap = []

    def add_num(self, num: int) -> None:
        # If the number is greater than or equal to the smallest number in min_heap, add it to min_heap.
        if not self.min_heap or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        # Otherwise, add it to max_heap (as a negative value to simulate max-heap behavior).
        else:
            heapq.heappush(self.max_heap, -num)

        # Balance the heaps to ensure their sizes differ by at most 1.
        if len(self.min_heap) > len(self.max_heap) + 1:
            # If min_heap has too many elements, move the smallest element from min_heap to max_heap.
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap):
            # If max_heap has too many elements, move the largest element from max_heap to min_heap.
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def find_median(self) -> float:
        # If both heaps have the same size, the median is the average of the two middle elements.
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        # If min_heap has more elements, the median is the smallest element in min_heap.
        return float(self.min_heap[0])

    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()
    def main(self):
        print("Command: MedianFinder()")
        median_finder = MedianFinder()
        print("Command: medianFinder.addNum(1)")
        median_finder.add_num(1)
        print("Command: medianFinder.addNum(2)")
        median_finder.add_num(2)
        print("Command: medianFinder.findMedian()")
        print(f"Output: {median_finder.find_median()}")
        print("Command: medianFinder.addNum(3)")
        median_finder.add_num(3)
        print("Command: medianFinder.findMedian()")
        print(f"Output: {median_finder.find_median()}")


if __name__ == "__main__":
    MedianFinder().main()

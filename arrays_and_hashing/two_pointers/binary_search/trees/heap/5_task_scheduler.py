import heapq
from collections import Counter, deque
from typing import List

# 621. Task Scheduler
# Medium

# Hint
# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.


# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:

# Input: tasks = ["A","A","A", "B","B","B"], n = 3

# Output: 10

# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.


# Constraints:


# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100
class Solution:
    # Time: O(n)
    # Space: O(1)
    def least_interval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)

        # Create a max heap
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        # Initialize the number of intervals (time units)
        intervals = 0

        # Queue to manage tasks during their cooldown period
        queue = deque()

        # Process tasks until both the heap and queue are empty
        while max_heap or queue:
            # Increment the interval count for each time unit
            intervals += 1

            if not max_heap:
                # If the heap is empty, skip to the next interval when the first task in the queue is ready
                intervals = queue[0][1]
            else:
                # Pop the most frequent task from the heap and decrement its count
                count = heapq.heappop(max_heap) + 1
                if count < 0:
                    # If the task still has remaining instances, add it to the cooldown queue
                    queue.append((count, intervals + n))

            # If the first task in the queue has completed its cooldown, push it back to the heap
            if queue and queue[0][1] == intervals:
                heapq.heappush(max_heap, queue.popleft()[0])

        # Return the total number of intervals required
        return intervals

    def main(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        print(f"Input: tasks = {tasks}, n = {n}")
        print(f"Output: {self.least_interval(tasks, n)}")

        tasks = ["A", "C", "A", "B", "D", "B"]
        n = 1
        print(f"Input: tasks = {tasks}, n = {n}")
        print(f"Output: {self.least_interval(tasks, n)}")

        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 3
        print(f"Input: tasks = {tasks}, n = {n}")
        print(f"Output: {self.least_interval(tasks, n)}")


if __name__ == "__main__":
    Solution().main()

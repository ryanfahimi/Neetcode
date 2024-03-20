from typing import List
from collections import deque

# 239. Sliding Window Maximum
# Hard

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.


# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length


class MaxSlidingWindow:
    # Time: O(k(n-k))
    def by_array(self, nums: List[int], k: int) -> List[int]:
        # Initialize the left and right pointers
        left, right = 0, k - 1

        # Initialize the max value and the max index
        max_value, max_index = max(nums[left : right + 1]), nums.index(
            max(nums[left : right + 1])
        )

        # Initialize the result array
        result = [max_value]

        # Slide the window over the array
        while right < len(nums) - 1:
            # Increment the left and right pointers
            left += 1
            right += 1

            # If the max index is within the window
            if max_index >= left:
                # Update the max value and the max index
                if nums[right] >= max_value:
                    max_value = nums[right]
                    max_index = right
            else:
                # Update the max value and the max index
                max_value = max(nums[left : right + 1])
                max_index = nums.index(max_value)

            # Append the max value to the result array
            result.append(max_value)

        return result

    def by_deque(self, nums: List[int], k: int) -> List[int]:
        # Initialize the deque
        dq = deque()

        # Initialize the result array
        result = []

        # Initialize the left pointer
        left = 0

        # Slide the window over the array
        for right, num in enumerate(nums):
            # If the deque is not empty and the current element is greater than the last element in the deque
            while dq and num > nums[dq[-1]]:
                # Pop the last element from the deque
                dq.pop()

            # Append the current index to the deque
            dq.append(right)

            # If the index at the front of the deque is out of the window
            if dq[0] < left:
                # Pop the front element from the deque
                dq.popleft()

            # If the window size is equal to k
            if (right + 1) >= k:
                # Append the element at the front of the deque to the result array
                result.append(nums[dq[0]])
                # Increment the left pointer
                left += 1

        return result

    def main(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Array Output: {self.by_array(nums, k)}")
        print(f"Deque Output: {self.by_deque(nums, k)}")

        nums = [1]
        k = 1
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Array Output: {self.by_array(nums, k)}")
        print(f"Deque Output: {self.by_deque(nums, k)}")


if __name__ == "__main__":
    MaxSlidingWindow().main()

from typing import List
from collections import Counter

# 347. Top K Frequent Elements
# Medium

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


class TopKFrequent:
    # Time: O(nlogn)
    # Space: O(n)
    def by_sorting(self, nums: List[int], k: int) -> List[int]:
        # Counter() returns a hash map
        count = Counter(nums)
        # sorted() returns a list
        # count.keys() is the iterable
        # key=lambda x: count[x] is the key function
        # count[x] is the value of the key
        # reverse=True sorts the list in descending order
        # [:k] returns the first k elements of the list
        return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]

    # Time: O(n)
    # Space: O(n)
    def by_bucket_sort(self, nums: List[int], k: int) -> List[int]:
        # Counter() returns a hash map
        nums_count = Counter(nums)
        # Create a list of empty lists
        bucket = [[] for _ in range(len(nums) + 1)]
        # Add the numbers to the list at the index of their frequency
        for num, nums_count in nums_count.items():
            bucket[nums_count].append(num)
        # Flatten the list of lists
        flat_list = [item for sublist in bucket for item in sublist]
        # Return the last k elements of the list
        return flat_list[-k:]

    def main(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Sorting Output: {self.by_sorting(nums, k)}")
        print(f"Bucket Sort Output: {self.by_bucket_sort(nums, k)}")

        nums = [1]
        k = 1
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Sorting Output: {self.by_sorting(nums, k)}")
        print(f"Bucket Sort Output: {self.by_bucket_sort(nums, k)}")


if __name__ == "__main__":
    TopKFrequent().main()

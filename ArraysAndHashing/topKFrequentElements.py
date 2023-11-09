import timeit
from typing import List
from collections import Counter
import heapq


class topKFrequentElements:
    # Time: O(nlogn)
    def sorted_hash_table(self, nums: List[int], k: int) -> List[int]:
        # Counter() returns a dictionary
        count = Counter(nums)
        # sorted() returns a list
        # count.keys() is the iterable
        # key=lambda x: count[x] is the key function
        # count[x] is the value of the key
        # reverse=True sorts the list in descending order
        # [:k] returns the first k elements of the list
        return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]

    # Time: O(nlogk)
    def hash_table_and_heap(self, nums: List[int], k: int) -> List[int]:
        # Counter() returns a dictionary
        count = Counter(nums)
        # heapq.nlargest() returns a list
        # k is the number of elements to return
        # count.keys() is the iterable
        # key=lambda x: count[x] is the key function
        # count[x] is the value of the key
        # heapq.nlargest() returns the first k elements of the list
        return heapq.nlargest(k, count.keys(), key=lambda x: count[x])

    # Time: O(n)
    def bucket_sort(self, nums: List[int], k: int) -> List[int]:
        # Counter() returns a dictionary
        count = Counter(nums)
        # Create a list of empty lists
        bucket = [[] for _ in range(len(nums) + 1)]
        # Add the numbers to the list at the index of their frequency
        for num, freq in count.items():
            bucket[freq].append(num)
        # Flatten the list of lists
        flat_list = [item for sublist in bucket for item in sublist]
        # Return the last k elements of the list
        return flat_list[-k:]

    def main(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        funcs = [self.sorted_hash_table, self.hash_table_and_heap, self.bucket_sort]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(nums, k))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    topKFrequentElements().main()

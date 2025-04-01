import heapq
from typing import List, Optional

from ListNode import ListNode

# 23. Merge k Sorted Lists
# Hard

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []


# Constraints:


# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.
class MergeKLists:
    # Time: O(nlogn)
    # Space: O(n)
    def by_brute_force(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize an empty list to store the nodes
        nodes = []

        # Traverse the list of lists
        for node in lists:
            # Start with the head of the list
            current = node

            # Traverse the list and store the nodes in the list
            while current:
                nodes.append(current)
                current = current.next

        # Sort the nodes based on their values
        nodes.sort(key=lambda x: x.val)

        # Initialize the dummy node
        dummy = ListNode()
        # Initialize the current node to the dummy node
        current = dummy

        # Iterate through the sorted nodes
        for node in nodes:
            # Set the next node to the current node
            current.next = node
            # Move to the next node
            current = current.next

        return dummy.next

    # Time: O(n*k)
    # Space: O(1)
    def by_iterative(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Base case: if the list of lists is empty, return None
        if not lists or len(lists) == 0:
            return None
        # Initialize a dummy node to simplify the code
        dummy = ListNode()
        # Initialize the current node to the dummy node
        current = dummy

        # Iterate while there are nodes in any of the lists
        while any(lists):
            # Initialize the minimum node and its index
            min_node = None
            min_index = None

            # Iterate through the list of lists
            for i, node in enumerate(lists):
                # If the node is not None and either min_node is None or the node's value is less than min_node's value
                if node and (min_node is None or node.val < min_node.val):
                    # Update the minimum node and its index
                    min_node = node
                    min_index = i

            # Set the next node to the current node
            current.next = min_node
            # Move to the next node
            current = current.next
            # Move to the next node in the list that had the minimum node
            lists[min_index] = min_node.next

        # Return the head of the merged list
        return dummy.next

    # Time: O(n*k)
    # Space: O(1)
    def by_one_by_one(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Base case: if the list of lists is empty, return None
        if not lists or len(lists) == 0:
            return None

        # Iterate through the list of lists
        for i in range(1, len(lists)):
            lists[0] = self.merge(lists[0], lists[i])

        return lists[0]

    # Time: O(nlogk)
    # Space: O(k)
    def by_heap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify the code
        dummy = ListNode()
        # Initialize the current node to the dummy node
        current = dummy
        # Initialize a heap to store the nodes
        heap = []

        # Iterate through the list of lists
        for i, node in enumerate(lists):
            # If the node is not None, push the value and the index to the heap
            if node:
                heapq.heappush(heap, (node.val, i))

        # Iterate while the heap is not empty
        while heap:
            # Pop the minimum value and its index from the heap
            val, i = heapq.heappop(heap)
            # Set the next node to the current node
            current.next = lists[i]
            # Move to the next node
            current = current.next
            # If the next node is not None, push the value and the index to the heap
            if lists[i].next:
                heapq.heappush(heap, (lists[i].next.val, i))
                # Move to the next node in the list
                lists[i] = lists[i].next

        # Return the head of the merged list
        return dummy.next

    # Time: O(nlogk)
    # Space: O(k)
    def by_iterative_divide_and_conquer(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # Base case: if the list of lists is empty, return None
        if not lists or len(lists) == 0:
            return None

        # Iterate while there is more than one list in the lists
        while len(lists) > 1:
            # Initialize a list to store the merged lists
            merged = []

            # Iterate through the list of lists in pairs
            for i in range(0, len(lists), 2):
                # If there is a pair of lists, merge them
                if i + 1 < len(lists):
                    merged.append(self.merge(lists[i], lists[i + 1]))
                # If there is only one list left, add it to the merged list
                else:
                    merged.append(lists[i])

            # Update the lists with the merged lists
            lists = merged

        return lists[0]

    # Time: O(nlogk)
    # Space: O(logk)
    def by_recursive_divide_and_conquer(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        def divide(left: int, right: int) -> Optional[ListNode]:
            # Base case: if left is greater than right, return None
            if left > right:
                return None
            # Base case: if left is equal to right, return the list at index left
            if left == right:
                return lists[left]

            # Calculate the middle index
            mid = left + (right - left) // 2
            # Recursively divide the lists into two halves
            l1 = divide(left, mid)
            l2 = divide(mid + 1, right)
            # Merge the two halves
            return self.merge(l1, l2)

        # Call the helper function with the left and right indices
        return divide(0, len(lists) - 1)

    # Helper function to merge two lists
    def merge(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Initialize a dummy node to simplify the code
        dummy = ListNode()
        # Initialize the current node to the dummy node
        current = dummy

        # Iterate through both lists
        while l1 and l2:
            # If the value in the first list is less than or equal to the value in the second list
            if l1.val <= l2.val:
                # Set the next node to the current node in the first list
                current.next = l1
                # Move to the next node in the first list
                l1 = l1.next
            else:
                # Set the next node to the current node in the second list
                current.next = l2
                # Move to the next node in the second list
                l2 = l2.next
            # Move to the next node in the merged list
            current = current.next

        # If there are any remaining nodes in the first list
        if l1:
            # Add the remaining nodes to the merged list
            current.next = l1
        # If there are any remaining nodes in the second list
        if l2:
            # Add the remaining nodes to the merged list
            current.next = l2

        # Return the head of the merged list
        return dummy.next

    def main(self):
        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
        print(f"Input: lists = {lists}")
        print(f"Output (Brute Force): {self.by_brute_force(lists)}")

        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
        print(f"Output (Iterative): {self.by_iterative(lists)}")

        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
        print(f"Output (One by One): {self.by_one_by_one(lists)}")

        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
        print(f"Output (Heap): {self.by_heap(lists)}")

        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
        print(
            f"Output (Iterative Divide and Conquer): {self.by_iterative_divide_and_conquer(lists)}"
        )

        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
        print(
            f"Output (Recursive Divide and Conquer): {self.by_recursive_divide_and_conquer(lists)}"
        )

        lists = []
        print(f"Input: lists = {lists}")
        print(f"Output (Brute Force): {self.by_brute_force(lists)}")
        print(f"Output (Iterative): {self.by_iterative(lists)}")
        print(f"Output (One by One): {self.by_one_by_one(lists)}")
        print(f"Output (Heap): {self.by_heap(lists)}")
        print(
            f"Output (Iterative Divide and Conquer): {self.by_iterative_divide_and_conquer(lists)}"
        )
        print(
            f"Output (Recursive Divide and Conquer): {self.by_recursive_divide_and_conquer(lists)}"
        )

        lists = [[]]
        print(f"Input: lists = {lists}")
        print(f"Output (Brute Force): {self.by_brute_force(lists)}")
        print(f"Output (Iterative): {self.by_iterative(lists)}")
        print(f"Output (One by One): {self.by_one_by_one(lists)}")
        print(f"Output (Heap): {self.by_heap(lists)}")
        print(
            f"Output (Iterative Divide and Conquer): {self.by_iterative_divide_and_conquer(lists)}"
        )
        print(
            f"Output (Recursive Divide and Conquer): {self.by_recursive_divide_and_conquer(lists)}"
        )


if __name__ == "__main__":
    MergeKLists().main()

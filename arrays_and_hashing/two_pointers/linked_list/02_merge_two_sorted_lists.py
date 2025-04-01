from typing import Optional

from ListNode import ListNode

# 21. Merge Two Sorted Lists
# Easy

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


class MergeTwoLists:
    # Time: O(n + m)
    # Space: O(1)
    def by_iterative(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Initialize a dummy node to simplify the code
        dummy = ListNode()
        # Initialize the current node to the dummy node
        current = dummy

        # Iterate through both lists
        while list1 and list2:
            # If the value in the first list is less than or equal to the value in the second list
            if list1.val <= list2.val:
                # Set the next node to the current node in the first list
                current.next = list1
                # Move to the next node in the first list
                list1 = list1.next
            else:
                # Set the next node to the current node in the second list
                current.next = list2
                # Move to the next node in the second list
                list2 = list2.next
            # Move to the next node in the merged list
            current = current.next

        # If there are any remaining nodes in the first list
        if list1:
            # Add the remaining nodes to the merged list
            current.next = list1
        # If there are any remaining nodes in the second list
        if list2:
            # Add the remaining nodes to the merged list
            current.next = list2

        # Return the head of the merged list
        return dummy.next

    # Time: O(n + m)
    # Space: O(n + m)
    def by_recursive(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # If either list is empty, return the other list
        if not list1:
            return list2
        if not list2:
            return list1

        # If the value in the first list is less than the value in the second list
        if list1.val < list2.val:
            # Set the next node to the current node in the first list
            list1.next = self.by_recursive(list1.next, list2)
            # Return the current node in the first list
            return list1
        else:
            # Set the next node to the current node in the second list
            list2.next = self.by_recursive(list1, list2.next)
            # Return the current node in the second list
            return list2

    def main(self):
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        print(f"Input: list1 = {list1}, list2 = {list2}")
        print(f"Output (Iterative): {self.by_iterative(list1, list2)}")

        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        print(f"Output (Recursive): {self.by_recursive(list1, list2)}")


if __name__ == "__main__":
    MergeTwoLists().main()

from typing import Optional

from ListNode import ListNode

# 206. Reverse Linked List
# Easy

# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []


# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


class ReverseList:
    # Time: O(n)
    # Space: O(1)
    def by_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize previous node to None
        prev = None
        # Start with the head of the list
        current = head
        # Iterate through the list
        while current:
            # Store the next node
            next = current.next
            # Reverse the current node's pointer
            current.next = prev
            # Move the previous node to the current node
            prev = current
            # Move to the next node in the list
            current = next
        # Return the new head of the reversed list
        return prev

    # Time: O(n)
    # Space: O(n)
    def by_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to reverse the list recursively
        def reverse(current: Optional[ListNode], prev: Optional[ListNode] = None):
            # Base case: if the current node is None, return the previous node
            if not current:
                return prev
            # Store the next node
            next = current.next
            # Reverse the current node's pointer
            current.next = prev
            # Recur for the next node
            return reverse(next, current)

        # Call the helper function with the head of the list
        return reverse(head)

    def main(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        print(f"Input: head = {head}")
        print(f"Output (Iterative): {self.by_iterative(head)}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        print(f"Output (Recursive): {self.by_recursive(head)}")

        head = ListNode(1, ListNode(2))
        print("Input: [1,2]")
        print(f"Output (Iterative): {self.by_iterative(head)}")

        head = ListNode(1, ListNode(2))
        print(f"Output (Recursive): {self.by_recursive(head)}")

        head = None
        print(f"Input: head = []")
        print(f"Output (Iterative): {self.by_iterative(head)}")
        print(f"Output (Recursive): {self.by_recursive(head)}")


if __name__ == "__main__":
    ReverseList().main()

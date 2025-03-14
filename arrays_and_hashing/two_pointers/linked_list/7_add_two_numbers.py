from ListNode import ListNode
from typing import Optional

# 2. Add Two Numbers
# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Constraints:


# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
class AddTwoNumbers:
    # Time: O(m + n)
    # Space: O(m + n)
    def by_recursive(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Helper function to add two numbers recursively
        def add(
            l1: Optional[ListNode], l2: Optional[ListNode], carry: int
        ) -> Optional[ListNode]:
            # Base case: if both lists are empty and there is no carry, return None
            if not l1 and not l2 and not carry:
                return None
            # Calculate the sum of the current nodes and the carry
            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            # Calculate the carry for the next iteration
            carry = value // 10
            # Create a new node with the value of the sum
            node = ListNode(value % 10)
            # Set the next node to the result of the next iteration
            node.next = add(l1.next if l1 else None, l2.next if l2 else None, carry)
            return node

        # Call the helper function with the input lists and carry value of 0
        return add(l1, l2, 0)

    # Time: O(m + n)
    # Space: O(1)
    def by_iterative(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Initialize a dummy node to simplify the code
        dummy = ListNode()
        # Initialize the current node to the dummy node
        current = dummy
        # Initialize the carry value to 0
        carry = 0

        # Iterate through both lists
        while l1 or l2 or carry:
            # Calculate the sum of the current nodes and the carry
            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            # Calculate the carry for the next iteration
            carry = value // 10
            # Create a new node with the value of the sum
            current.next = ListNode(value % 10)
            # Move to the next node in the merged list
            current = current.next
            # Move to the next node in the input lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the next node of the dummy node
        return dummy.next

    def main(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        print(f"Input: l1 = {l1}, l2 = {l2}")
        print(f"Output (Recursive): {self.by_recursive(l1, l2)}")
        print(f"Output (Iterative): {self.by_iterative(l1, l2)}")

        l1 = ListNode(0)
        l2 = ListNode(0)
        print(f"Input: l1 = {l1}, l2 = {l2}")
        print(f"Output (Recursive): {self.by_recursive(l1, l2)}")
        print(f"Output (Iterative): {self.by_iterative(l1, l2)}")

        l1 = ListNode(
            9,
            ListNode(
                9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
            ),
        )
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        print(f"Input: l1 = {l1}, l2 = {l2}")
        print(f"Output (Recursive): {self.by_recursive(l1, l2)}")
        print(f"Output (Iterative): {self.by_iterative(l1, l2)}")


if __name__ == "__main__":
    AddTwoNumbers().main()

from typing import Optional
from ListNode import ListNode

# 25. Reverse Nodes in k-Group
# Hard

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]


# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000


# Follow-up: Can you solve the problem in O(1) extra memory space?
class ReverseKGroup:
    # Time: O(n)
    # Space: O(n/k)
    def by_recursive(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        counter = 0
        # Find the k+1 node
        while current and counter != k:
            current = current.next
            counter += 1

        # If k+1 node is found
        if counter == k:
            # Reverse list with k+1 node as head
            current = self.by_recursive(current, k)
            # Reverse current k-group
            while counter:
                # Store the next node
                next = head.next
                # Reverse the current node's pointer
                head.next = current
                # Move to the next node
                current = head
                # Move to the next node
                head = next
                counter -= 1
            head = current

        return head

    # Time: O(n)
    # Space: O(1)
    def by_iterative(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, tail):
            # Initialize the previous node to the node after the tail
            prev = tail.next
            current = head
            # Reverse the nodes until we reach the tail
            while prev != tail:
                next = current.next
                current.next = prev
                prev = current
                current = next
            # Return the new head and tail
            return tail, head

        # Create a dummy node to handle edge cases
        dummy = ListNode(next=head)
        prev = tail = dummy
        while head:
            # Move the tail pointer k nodes ahead
            for _ in range(k):
                tail = tail.next
            # If there are fewer than k nodes left, return the result
            if not tail:
                return dummy.next
            # Store the next head for the next group
            next_head = tail.next
            # Reverse the current k-group
            head, tail = reverse(head, tail)
            # Connect the previous group with the reversed group
            prev.next = head
            tail.next = next_head
            # Move the prev and head pointers to the next group
            prev = tail
            head = next_head
        return dummy.next

    def main(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        k = 2
        print(f"Input: head = {head}, k = {k}")
        print(f"Output (Recursive): {self.by_recursive(head, k)}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        print(f"Output (Iterative): {self.by_iterative(head, k)}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        k = 3
        print(f"Input: head = {head}, k = {k}")
        print(f"Output (Recursive): {self.by_recursive(head, k)}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        print(f"Output (Iterative): {self.by_iterative(head, k)}")


if __name__ == "__main__":
    ReverseKGroup().main()

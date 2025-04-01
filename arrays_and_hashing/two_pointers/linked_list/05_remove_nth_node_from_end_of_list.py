from ListNode import ListNode
from typing import Optional

# 19. Remove Nth Node From End of List
# Medium

# Hint
# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Follow up: Could you do this in one pass?
class RemoveNthFromEnd:
    # Time: O(n)
    # Space: O(n)
    def by_brute_force(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize an empty list to store the nodes
        nodes = []

        # Start with the head of the list
        current = head

        # Traverse the list and store the nodes in the list
        while current:
            nodes.append(current)
            current = current.next

        # Calculate the index of the node to be removed
        remove_index = len(nodes) - n

        # If the node to be removed is the first node
        if remove_index == 0:
            return head.next

        # Remove the node from the list
        nodes[remove_index - 1].next = nodes[remove_index].next

        return head

    # Time: O(n)
    # Space: O(n)
    def by_recursive(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Helper function to remove the nth node from the end of the list recursively
        def remove(node: Optional[ListNode]) -> int:
            # Base case: if the current node is None, return 0
            if not node:
                return 0

            # Recursively remove the nth node from the end of the list
            index = remove(node.next)

            # If the index is equal to n, remove the current node
            if index == n:
                node.next = node.next.next

            # Return the index of the current node
            return index + 1

        # Initialize a dummy node to simplify the code
        dummy = ListNode(next=head)

        # Remove the nth node from the end of the list
        remove(dummy)

        return dummy.next

    # Time: O(n)
    # Space: O(1)
    def by_two_passes(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize a dummy node to simplify the code
        dummy = ListNode(next=head)

        # Initialize the length of the list
        length = 0
        current = head

        # Calculate the length of the list
        while current:
            length += 1
            current = current.next

        # Calculate the index of the node to be removed
        remove_index = length - n
        current = dummy

        # Traverse the list to the node before the one to be removed
        while remove_index > 0:
            remove_index -= 1
            current = current.next

        # Remove the node from the list
        current.next = current.next.next

        return dummy.next

    # Time: O(n)
    # Space: O(1)
    def by_one_pass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize a dummy node to simplify the code
        dummy = ListNode(next=head)

        # Initialize the left and right pointers
        left, right = dummy, head

        # Move the right pointer n steps ahead
        while n > 0:
            right = right.next
            n -= 1

        # Move both pointers until the right pointer reaches the end of the list
        while right:
            left = left.next
            right = right.next

        # Remove the node from the list
        left.next = left.next.next

        return dummy.next

    def main(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        n = 2
        print(f"Input: head = {head}, n = {n}")
        print(f"Output: (Brute Force) {self.by_brute_force(head, n)}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        print(f"Output: (Recursive) {self.by_recursive(head, n)}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        print(f"Output: (Two Pass) {self.by_two_passes(head, n)}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        print(f"Output: (One Pass) {self.by_one_pass(head, n)}")

        head = ListNode(1)
        n = 1
        print(f"Input: head = {head}, n = {n}")

        head = ListNode(1)
        print(f"Output (Brute Force): {self.by_brute_force(head, n)}")

        head = ListNode(1)
        print(f"Output (Recursive): {self.by_recursive(head, n)}")

        head = ListNode(1)
        print(f"Output (Two Pass): {self.by_two_passes(head, n)}")

        head = ListNode(1)
        print(f"Output (One Pass): {self.by_one_pass(head, n)}")

        head = ListNode(1, ListNode(2))
        n = 1
        print(f"Input: head = {head}, n = {n}")
        print(f"Output (Brute Force): {self.by_brute_force(head, n)}")

        head = ListNode(1, ListNode(2))
        print(f"Output (Recursive): {self.by_recursive(head, n)}")

        head = ListNode(1, ListNode(2))
        print(f"Output (Two Pass): {self.by_two_passes(head, n)}")

        head = ListNode(1, ListNode(2))
        print(f"Output (One Pass): {self.by_one_pass(head, n)}")


if __name__ == "__main__":
    RemoveNthFromEnd().main()

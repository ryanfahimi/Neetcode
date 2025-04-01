from ListNode import ListNode
from typing import Optional

# 143. Reorder List
# Medium

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Reorder the list in-place.


# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]


# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000


class ReorderList:
    # Time: O(n)
    # Space: O(n)
    def by_brute_force(self, head: Optional[ListNode]) -> None:
        # Initialize an empty list to store the nodes
        nodes = []
        # Start with the head of the list
        current = head

        # Traverse the list and store the nodes in the list
        while current:
            nodes.append(current)
            current = current.next

        # Initialize the left and right pointers
        left = 0
        right = len(nodes) - 1

        # Iterate through the list
        while left < right:
            # Set the next node of the left pointer to the right node
            nodes[left].next = nodes[right]
            # Move the left pointer to the next node
            left += 1

            # If the left pointer is equal to the right pointer, break the loop
            if left == right:
                break

            # Set the next node of the right pointer to the left node
            nodes[right].next = nodes[left]
            # Move the right pointer to the previous node
            right -= 1

        # Set the next node of the last node to None
        nodes[left].next = None

    # Time: O(n)
    # Space: O(n)
    def by_recursive(self, head: Optional[ListNode]) -> None:
        def reorder(
            root: Optional[ListNode], current: Optional[ListNode]
        ) -> Optional[ListNode]:
            # Base case: if current is None, return root
            if not current:
                return root

            # Recursively call reorder with the next node
            root = reorder(root, current.next)

            # If root is None, return None
            if not root:
                return None

            temp = None
            # If root is the same as current or root's next is current, set current's next to None
            if root == current or root.next == current:
                current.next = None
            else:
                # Otherwise, reorder the nodes
                temp = root.next
                root.next = current
                current.next = temp

            # Return the next node to be processed
            return temp

        # If the head is not None, start the reordering process
        if head:
            head = reorder(head, head.next)

    # Time: O(n)
    # Space: O(1)
    def by_reverse_and_merge(self, head: Optional[ListNode]) -> None:
        # Initialize two pointers, slow and fast
        slow, fast = head, head
        # Move slow pointer by 1 step and fast pointer by 2 steps to find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev, current = None, slow
        while current:
            current.next, prev, current = prev, current, current.next

        # Merge the two halves
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

    def main(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.by_brute_force(head)
        print(f"Input: head = {head}")
        print(f"Output (Brute Force): {head}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.by_recursive(head)
        print(f"Output (Recursive): {head}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.by_reverse_and_merge(head)
        print(f"Output (Reverse and Merge): {head}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.by_brute_force(head)
        print(f"Input: head = {head}")
        print(f"Output (Brute Force): {head}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.by_recursive(head)
        print(f"Output (Recursive): {head}")

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.by_reverse_and_merge(head)
        print(f"Output (Reverse and Merge): {head}")


if __name__ == "__main__":
    ReorderList().main()

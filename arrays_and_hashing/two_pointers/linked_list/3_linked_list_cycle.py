from typing import Optional

from ListNode import ListNode

# 141. Linked List Cycle
# Easy

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.


# Follow up: Can you solve it using O(1) (i.e. constant) memory?
class Solution:
    # Time: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, slow and fast, both starting at the head of the linked list
        slow = head
        fast = head

        # Traverse the linked list with two pointers
        while fast and fast.next:
            # Move slow pointer by one step
            slow = slow.next
            # Move fast pointer by two steps
            fast = fast.next.next

            # If slow and fast pointers meet, there is a cycle
            if slow == fast:
                return True

        # If we reach here, there is no cycle in the linked list
        return False

    def main(self):
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(-4)
        head.next.next.next.next = head.next
        print(f"Input: head = [3,2,0,-4], pos = 1")
        print(f"Output: {self.hasCycle(head)}")

        head = ListNode(1, ListNode(2))
        head.next.next = head
        print(f"Input: head = [1,2], pos = 0")
        print(f"Output: {self.hasCycle(head)}")

        head = ListNode(1)
        print(f"Input: head = [1], pos = -1")
        print(f"Output: {self.hasCycle(head)}")


if __name__ == "__main__":
    Solution().main()

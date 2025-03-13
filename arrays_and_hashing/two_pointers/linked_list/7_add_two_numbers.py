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
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = False

        while l1 and l2:
            sum = 0
            if carry:
                sum += 1
            carry = False
            sum += l1.val + l2.val
            if sum >= 10:
                sum -= 10
                carry = True
            current.next = ListNode(sum)
            current = current.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            current.next = l1
            if carry:
                l1.val += 1
            carry = False
            if l1.val >= 10:
                l1.val -= 10
                carry = True
            l1 = l1.next
            current = current.next
        while l2:
            current.next = l2
            if carry:
                l2.val += 1
            carry = False
            if l2.val >= 10:
                l2.val -= 10
                carry = True
            l2 = l2.next
            current = current

        if carry:
            current.next = ListNode(1)

        return dummy.next

    def main(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        print(f"Input: l1 = {l1}, l2 = {l2}")
        print(f"Output: {self.addTwoNumbers(l1, l2)}")

        l1 = ListNode(0)
        l2 = ListNode(0)
        print(f"Input: l1 = {l1}, l2 = {l2}")
        print(f"Output: {self.addTwoNumbers(l1, l2)}")

        l1 = ListNode(
            9,
            ListNode(
                9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
            ),
        )
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        print(f"Input: l1 = {l1}, l2 = {l2}")
        print(f"Output: {self.addTwoNumbers(l1, l2)}")


if __name__ == "__main__":
    Solution().main()

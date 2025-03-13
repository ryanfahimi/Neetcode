# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Value of the node
        self.next = next  # Pointer to the next node

    def __repr__(self):
        if self.next:
            return f"{self.val} -> {self.next}"
        return str(self.val)

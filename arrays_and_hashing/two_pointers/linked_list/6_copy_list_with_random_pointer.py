import collections
from typing import Optional

# 138. Copy List with Random Pointer
# Medium

# Hint
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.


# Example 1:


# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:


# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:


# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]


# Constraints:

# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        if self.next:
            return f"Val: {self.val}, Rand: {self.random.val if self.random else None} -> {self.next}"
        return f"Val: {self.val}, Rand: {self.random.val if self.random else None}"


class CopyRandomList:
    # Time: O(n)
    # Space: O(n)
    def by_recursion(self, head: Optional[Node]) -> Optional[Node]:
        def copy_node(node: Optional[Node], visited: dict) -> Optional[Node]:
            # Base case: if the current node is None, return None
            if not node:
                return None

            # If the current node is already copied, return the copied node
            if node in visited:
                return visited[node]

            # Create a new node with the value of the current node
            copy = Node(node.val)
            # Store the copied node in the visited dictionary
            visited[node] = copy

            # Recursively copy the next node
            copy.next = copy_node(node.next, visited)
            # Set the random pointer of the copied node
            copy.random = visited[node.random]

            return copy

        # Start the recursion with the head node and an empty visited dictionary
        return copy_node(head, {None: None})

    # Time: O(n)
    # Space: O(n)
    def by_two_passes(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # Create a dictionary to hold the mapping from original nodes to their copies
        visited = {None: None}
        current = head

        # First pass: create a copy of each node and store it in the dictionary
        while current:
            visited[current] = Node(current.val)
            current = current.next

        current = head

        # Second pass: assign next and random pointers for the copied nodes
        while current:
            copy = visited[current]
            copy.next = visited[current.next]
            copy.random = visited[current.random]
            current = current.next

        return visited[head]

    # Time: O(n)
    # Space: O(n)
    def by_one_pass(self, head: Optional[Node]) -> Optional[Node]:
        # Create a defaultdict to hold the mapping from original nodes to their copies
        visited = collections.defaultdict(lambda: Node(0))
        visited[None] = None

        current = head
        # Iterate through the original list to create copies of each node
        while current:
            # Set the value of the copied node
            visited[current].val = current.val
            # Set the next pointer of the copied node
            visited[current].next = visited[current.next]
            # Set the random pointer of the copied node
            visited[current].random = visited[current.random]
            # Move to the next node in the original list
            current = current.next

        # Return the head of the copied linked list
        return visited[head]

    # Time: O(n)
    # Space: O(1)
    def by_optimized(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # First pass: create a copy of each node and insert it right next to the original node
        current = head
        while current:
            copy = Node(current.val)
            copy.next = current.next
            current.next = copy
            current = copy.next

        # Second pass: assign random pointers for the copied nodes
        current = head
        while current:
            current.next.random = current.random.next if current.random else None
            current = current.next.next

        # Third pass: restore the original list and extract the copied list
        new_head = head.next
        current = head
        while current:
            copy = current.next
            current.next = copy.next
            current = copy.next
            copy.next = current.next if current else None

        return new_head

    def main(self):
        head = Node(7, Node(13, Node(11, Node(10, Node(1)))))
        head.next.random = head
        head.next.next.random = head.next.next.next.next
        head.next.next.next.random = head.next.next
        head.next.next.next.next.random = head
        print(f"Input: head = {head}")
        print(f"Output (Recursion): {self.by_recursion(head)}")
        print(f"Output (Two Passes): {self.by_two_passes(head)}")
        print(f"Output (One Pass): {self.by_one_pass(head)}")
        print(f"Output (Optimized): {self.by_optimized(head)}")

        head = Node(1, Node(2))
        head.random = head.next
        head.next.random = head.next
        print(f"Input: head = {head}")
        print(f"Output (Recursion): {self.by_recursion(head)}")
        print(f"Output (Two Passes): {self.by_two_passes(head)}")
        print(f"Output (One Pass): {self.by_one_pass(head)}")
        print(f"Output (Optimized): {self.by_optimized(head)}")

        head = Node(3, Node(3, Node(3)))
        head.next.random = head
        print(f"Input: head = {head}")
        print(f"Output (Recursion): {self.by_recursion(head)}")
        print(f"Output (Two Passes): {self.by_two_passes(head)}")
        print(f"Output (One Pass): {self.by_one_pass(head)}")
        print(f"Output (Optimized): {self.by_optimized(head)}")


if __name__ == "__main__":
    CopyRandomList().main()

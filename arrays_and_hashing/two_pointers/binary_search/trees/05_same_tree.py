from collections import deque
from typing import Optional

from TreeNode import TreeNode

# 100. Same Tree
# Easy

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false


# Constraints:


# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104
class IsSameTree:
    # Time: O(n)
    # Space: O(n)
    def by_bfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both trees are empty
        if not p and not q:
            return True

        # Initialize a queue with the root nodes of both trees
        queue = deque([(p, q)])

        while queue:
            # Pop the front pair of nodes from the queue
            p_node, q_node = queue.popleft()

            # If both nodes are None, continue to the next pair
            if not p_node and not q_node:
                continue

            # If one of the nodes is None or their values are different, the trees are not the same
            if not p_node or not q_node or p_node.val != q_node.val:
                return False

            # Append the left children of both nodes to the queue
            queue.append((p_node.left, q_node.left))
            # Append the right children of both nodes to the queue
            queue.append((p_node.right, q_node.right))

        # If all nodes matched, the trees are the same
        return True

    # Time: O(n)
    # Space: O(n)
    def by_recursive_dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both trees are empty
        if not p and not q:
            return True

        # Check if both nodes are not None, their values are equal, and recursively check their children
        return (
            p is not None
            and q is not None
            and p.val == q.val
            and self.by_recursive_dfs(p.left, q.left)
            and self.by_recursive_dfs(p.right, q.right)
        )

    # Time: O(n)
    # Space: O(n)
    def by_iterative_dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both trees are empty
        if not p and not q:
            return True

        # Initialize a stack with the root nodes of both trees
        stack = [(p, q)]

        while stack:
            # Pop the top pair of nodes from the stack
            p_node, q_node = stack.pop()

            # If both nodes are None, continue to the next pair
            if not p_node and not q_node:
                continue

            # If one of the nodes is None or their values are different, the trees are not the same
            if not p_node or not q_node or p_node.val != q_node.val:
                return False

            # Append the right children of both nodes to the stack
            stack.append((p_node.right, q_node.right))
            # Append the left children of both nodes to the stack
            stack.append((p_node.left, q_node.left))

        # If all nodes matched, the trees are the same
        return True

    def main(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        print(f"Input: p = {p}, q = {q}")
        print(f"Output: (BFS) {self.by_bfs(p, q)}")
        print(f"Output: (Recursive DFS) {self.by_recursive_dfs(p, q)}")
        print(f"Output: (Iterative DFS) {self.by_iterative_dfs(p, q)}")

        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        print(f"Input: p = {p}, q = {q}")
        print(f"Output: (BFS) {self.by_bfs(p, q)}")
        print(f"Output: (Recursive DFS) {self.by_recursive_dfs(p, q)}")
        print(f"Output: (Iterative DFS) {self.by_iterative_dfs(p, q)}")

        p = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(1, TreeNode(1), TreeNode(2)))
        q = TreeNode(1, TreeNode(2, TreeNode(1)), TreeNode(1, None, TreeNode(2)))
        print(f"Input: p = {p}, q = {q}")
        print(f"Output: (BFS) {self.by_bfs(p, q)}")
        print(f"Output: (Recursive DFS) {self.by_recursive_dfs(p, q)}")
        print(f"Output: (Iterative DFS) {self.by_iterative_dfs(p, q)}")


if __name__ == "__main__":
    IsSameTree().main()

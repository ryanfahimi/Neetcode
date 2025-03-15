from collections import deque
from typing import Optional

from TreeNode import TreeNode

# 104. Maximum Depth of Binary Tree
# Easy

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2


# Constraints:


# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100
class MaxDepth:
    # Time: O(n)
    # Space: O(n)
    def by_bfs(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            # If the tree is empty, return depth as 0
            return 0

        # Initialize a queue for BFS and add the root node
        queue = deque([root])
        # Initialize depth counter
        depth = 0

        # Loop until the queue is empty
        while queue:
            # Increment depth for each level of the tree
            depth += 1

            # Process all nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()

                # Add left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                # Add right child to the queue if it exists
                if node.right:
                    queue.append(node.right)

        # Return the maximum depth of the tree
        return depth

    # Time: O(n)
    # Space: O(n)
    def by_recursive_dfs(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0

        # Recursively calculate the depth of the left and right subtrees
        left_depth = self.by_recursive_dfs(root.left)
        right_depth = self.by_recursive_dfs(root.right)

        # Return the maximum depth of the left and right subtrees
        return max(left_depth, right_depth) + 1

    # Time: O(n)
    # Space: O(n)
    def by_iterative_dfs(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            # If the tree is empty, return depth as 0
            return 0

        # Initialize a stack for DFS with the root node and its depth
        stack = [(root, 1)]
        # Initialize max_depth to keep track of the maximum depth
        max_depth = 0

        # Loop until the stack is empty
        while stack:
            # Pop a node and its depth from the stack
            node, depth = stack.pop()
            # Update max_depth if the current depth is greater
            max_depth = max(max_depth, depth)

            # Add left child to the stack if it exists, with incremented depth
            if node.left:
                stack.append((node.left, depth + 1))
            # Add right child to the stack if it exists, with incremented depth
            if node.right:
                stack.append((node.right, depth + 1))

        # Return the maximum depth of the tree
        return max_depth

    def main(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (Recursive DFS): {self.by_recursive_dfs(root)}")
        print(f"Output (Iterative DFS): {self.by_iterative_dfs(root)}")

        root = TreeNode(1, None, TreeNode(2))
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (Recursive DFS): {self.by_recursive_dfs(root)}")
        print(f"Output (Iterative DFS): {self.by_iterative_dfs(root)}")


if __name__ == "__main__":
    MaxDepth().main()

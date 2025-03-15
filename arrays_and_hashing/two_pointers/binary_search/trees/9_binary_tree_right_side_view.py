from collections import deque
from typing import List, Optional

from TreeNode import TreeNode

# 199. Binary Tree Right Side View
# Medium

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


# Example 1:

# Input: root = [1,2,3,null,5,null,4]

# Output: [1,3,4]

# Explanation:


# Example 2:

# Input: root = [1,2,3,4,null,null,null,5]

# Output: [1,3,4,5]

# Explanation:


# Example 3:

# Input: root = [1,null,3]

# Output: [1,3]

# Example 4:

# Input: root = []

# Output: []


# Constraints:


# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
class RightSideView:
    # Time: O(n)
    # Space: O(n)
    def by_bfs(self, root: Optional[TreeNode]) -> List[int]:
        # Base case
        if not root:
            return []

        # Initialize a queue for BFS and add the root node
        queue = deque([root])
        # Initialize the right side view list
        right_side = []

        # Loop until the queue is empty
        while queue:
            # Process all nodes at the current level
            for i in range(len(queue)):
                node = queue.popleft()

                # Add the rightmost node's value to the right side view list
                if i == 0:
                    right_side.append(node.val)

                # Add right child to the queue if it exists
                if node.right:
                    queue.append(node.right)
                # Add left child to the queue if it exists
                if node.left:
                    queue.append(node.left)

        return right_side

    # Time: O(n)
    # Space: O(n)
    def by_dfs(self, root: Optional[TreeNode]) -> List[int]:
        # Helper function to recursively traverse the tree
        def traverse(node, level):
            # Base case
            if not node:
                return

            # If the current level is equal to the length of the right side view list
            if level == len(right_side):
                # Add the current node's value to the right side view list
                right_side.append(node.val)

            # Recursively traverse the right subtree first
            traverse(node.right, level + 1)
            # Recursively traverse the left subtree
            traverse(node.left, level + 1)

        # Base case
        if not root:
            return []

        # Initialize the right side view list
        right_side = []
        # Start the DFS traversal from the root node
        traverse(root, 0)

        return right_side

    def main(self):
        root = TreeNode(
            1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4))
        )
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")

        root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5)), TreeNode(3)))
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")

        root = TreeNode(1, None, TreeNode(3))
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")

        root = None
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")


if __name__ == "__main__":
    RightSideView().main()

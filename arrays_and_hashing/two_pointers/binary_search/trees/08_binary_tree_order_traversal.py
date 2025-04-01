from collections import deque
from typing import List, Optional

from TreeNode import TreeNode

# 102. Binary Tree Level Order Traversal
# Medium

# Hint
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []


# Constraints:


# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
class LevelOrder:
    # Time: O(n)
    # Space: O(n)
    def by_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Base case
        if not root:
            return []

        # Initialize a queue for BFS and add the root node
        queue = deque([root])
        # Initialize the levels list
        levels = []

        # Loop until the queue is empty
        while queue:
            # Initialize the level list
            level = []
            # Process all nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()
                # Add the node's value to the level list
                level.append(node.val)

                # Add left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                # Add right child to the queue if it exists
                if node.right:
                    queue.append(node.right)

            # Add the level list to the levels list
            levels.append(level)

        return levels

    # Time: O(n)
    # Space: O(n)
    def by_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Helper function to recursively traverse the tree
        def traverse(node, level):
            # Base case
            if not node:
                return

            # If the level list does not exist, create it
            if len(levels) == level:
                levels.append([])

            # Add the node's value to the level list
            levels[level].append(node.val)

            # Recursively traverse the left and right subtrees
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        # Base case
        if not root:
            return []

        # Initialize the levels list
        levels = []
        # Start the DFS traversal from the root node
        traverse(root, 0)

        return levels

    def main(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")

        root = TreeNode(1)
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")

        root = None
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")


if __name__ == "__main__":
    LevelOrder().main()

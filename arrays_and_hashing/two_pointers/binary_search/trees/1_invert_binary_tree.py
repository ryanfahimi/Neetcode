from collections import deque
from typing import Optional
from TreeNode import TreeNode

# 226. Invert Binary Tree
# Easy

# Given the root of a binary tree, invert the tree, and return its root.


# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


class InvertTree:
    # Time: O(n)
    # Space: O(n)
    def bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            # Swap the left and right children
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

    # Time: O(n)
    # Space: O(n)
    def recursive_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None

        # Swap the left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right children
        self.recursive_dfs(root.left)
        self.recursive_dfs(root.right)

        return root

    # Time: O(n)
    # Space: O(n)
    def iterative_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()

            # Swap the left and right children
            node.left, node.right = node.right, node.left

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return root

    def main(self):
        root = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        )
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.bfs(root)}")

        root = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        )
        print(f"Output (Recursive DFS): {self.recursive_dfs(root)}")

        root = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        )
        print(f"Output (Iterative DFS): {self.iterative_dfs(root)}")

        root = TreeNode(2, TreeNode(1), TreeNode(3))
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.bfs(root)}")

        root = TreeNode(2, TreeNode(1), TreeNode(3))
        print(f"Output (Recursive DFS): {self.recursive_dfs(root)}")

        root = TreeNode(2, TreeNode(1), TreeNode(3))
        print(f"Output (Iterative DFS): {self.iterative_dfs(root)}")

        root = None
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.bfs(root)}")
        print(f"Output (Recursive DFS): {self.bfs(root)}")
        print(f"Output (Iterative DFS): {self.bfs(root)}")


if __name__ == "__main__":
    InvertTree().main()

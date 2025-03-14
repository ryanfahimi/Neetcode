from typing import Optional

from TreeNode import TreeNode

# 543. Diameter of Binary Tree
# Easy

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1


# Constraints:


# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100
class DiameterOfBinaryTree:
    def brute_force(self, root: Optional[TreeNode]) -> int:
        def max_height(node):
            if not node:
                return 0

            return 1 + max(max_height(node.left), max_height(node.right))

        # Base case
        if not root:
            return 0

        left_height = max_height(root.left)
        right_height = max_height(root.right)

        # Calculate the diameter of the left subtree
        left_diameter = self.brute_force(root.left)
        # Calculate the diameter of the right subtree
        right_diameter = self.brute_force(root.right)

        # Return the maximum of the left diameter, right diameter, and the sum of the heights of the left and right subtrees
        return max(left_height + right_height, left_diameter, right_diameter)

    # Time: O(n)
    # Space: O(n)
    def recursive_dfs(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0

        # Initialize the diameter of the tree
        diameter = 0

        # Recursive function to calculate the height of the tree
        def dfs(node):
            # Base case
            if not node:
                return 0

            # Recursively calculate the height of the left subtree
            left = dfs(node.left)
            # Recursively calculate the height of the right subtree
            right = dfs(node.right)

            # Update the diameter of the tree
            nonlocal diameter
            diameter = max(diameter, left + right)

            # Return the height of the current node
            return 1 + max(left, right)

        dfs(root)

        return diameter

    def iterative_dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        heights = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in heights:
                stack.append(node.left)
            elif node.right and node.right not in heights:
                stack.append(node.right)
            else:
                node = stack.pop()

                left_height, left_diameter = heights[node.left]
                right_height, right_diameter = heights[node.right]

                heights[node] = (
                    1 + max(left_height, right_height),
                    max(left_height + right_height, left_diameter, right_diameter),
                )

        return heights[root][1]

    def main(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        print(f"Input: root = {root}")
        print(f"Output (Brute Force): {self.brute_force(root)}")
        print(f"Output (Recursive DFS): {self.recursive_dfs(root)}")
        print(f"Output (Iterative DFS): {self.iterative_dfs(root)}")

        root = TreeNode(1, TreeNode(2))
        print(f"Input: root = {root}")
        print(f"Output (Brute Force): {self.brute_force(root)}")
        print(f"Output (Recursive DFS): {self.recursive_dfs(root)}")
        print(f"Output (Iterative DFS): {self.iterative_dfs(root)}")


if __name__ == "__main__":
    DiameterOfBinaryTree().main()

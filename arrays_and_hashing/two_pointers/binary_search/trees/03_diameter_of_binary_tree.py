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
    # Time: O(n^2)
    # Space: O(n)
    def by_brute_force(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0

            return 1 + max(height(node.left), height(node.right))

        # Base case
        if not root:
            return 0

        left_height = height(root.left)
        right_height = height(root.right)

        # Calculate the diameter of the left subtree
        left_diameter = self.by_brute_force(root.left)
        # Calculate the diameter of the right subtree
        right_diameter = self.by_brute_force(root.right)

        # Return the maximum of the left diameter, right diameter, and the sum of the heights of the left and right subtrees
        return max(left_height + right_height, left_diameter, right_diameter)

    # Time: O(n)
    # Space: O(n)
    def by_recursive_dfs(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0

        # Initialize the diameter of the tree
        diameter = 0

        # Recursive function to calculate the height of the tree
        def height(node):
            # Base case
            if not node:
                return 0

            # Recursively calculate the height of the left subtree
            left = height(node.left)
            # Recursively calculate the height of the right subtree
            right = height(node.right)

            # Update the diameter of the tree
            nonlocal diameter
            diameter = max(diameter, left + right)

            # Return the height of the current node
            return 1 + max(left, right)

        height(root)

        return diameter

    # Time: O(n)
    # Space: O(n)
    def by_iterative_dfs(self, root: Optional[TreeNode]) -> int:
        # Base case: if the root is None, the diameter is 0
        if not root:
            return 0

        # Initialize the stack with the root node
        stack = [root]
        # Dictionary to store the heights and diameters of the nodes
        heights = {None: (0, 0)}

        # Iterate while there are nodes in the stack
        while stack:
            node = stack[-1]

            # If the left child exists and its height is not calculated, push it to the stack
            if node.left and node.left not in heights:
                stack.append(node.left)
            # If the right child exists and its height is not calculated, push it to the stack
            elif node.right and node.right not in heights:
                stack.append(node.right)
            else:
                # Pop the node from the stack
                node = stack.pop()

                # Get the heights and diameters of the left and right children
                left_height, left_diameter = heights[node.left]
                right_height, right_diameter = heights[node.right]

                # Calculate the height and diameter of the current node
                heights[node] = (
                    1 + max(left_height, right_height),
                    max(left_height + right_height, left_diameter, right_diameter),
                )

        # Return the diameter of the root node
        return heights[root][1]

    def main(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        print(f"Input: root = {root}")
        print(f"Output (Brute Force): {self.by_brute_force(root)}")
        print(f"Output (Recursive DFS): {self.by_recursive_dfs(root)}")
        print(f"Output (Iterative DFS): {self.by_iterative_dfs(root)}")

        root = TreeNode(1, TreeNode(2))
        print(f"Input: root = {root}")
        print(f"Output (Brute Force): {self.by_brute_force(root)}")
        print(f"Output (Recursive DFS): {self.by_recursive_dfs(root)}")
        print(f"Output (Iterative DFS): {self.by_iterative_dfs(root)}")


if __name__ == "__main__":
    DiameterOfBinaryTree().main()

from typing import Optional

from TreeNode import TreeNode

# 110. Balanced Binary Tree
# Easy

# Given a binary tree, determine if it is height-balanced.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true


# Constraints:


# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104
class IsBalanced:
    # Time: O(n^2)
    # Space: O(n)
    def by_brute_force(self, root: Optional[TreeNode]) -> bool:
        # Helper function to calculate the height of a subtree
        def height(node):
            if not node:  # If the node is None, its height is 0
                return 0

            # Recursively calculate the height of the left and right subtrees
            return 1 + max(height(node.left), height(node.right))

        if not root:  # If the root is None, the tree is balanced
            return True

        # Calculate the height of the left and right subtrees
        left_height = height(root.left)
        right_height = height(root.right)

        # Check if the current node is balanced and recursively check its subtrees
        return (
            abs(left_height - right_height)
            <= 1  # Check if the height difference is <= 1
            and self.by_brute_force(root.left)  # Recursively check the left subtree
            and self.by_brute_force(root.right)  # Recursively check the right subtree
        )

    # Time: O(n)
    # Space: O(n)
    def by_recursive_dfs(self, root: Optional[TreeNode]) -> bool:
        # Helper function to calculate the height of a subtree
        def height(node):
            if not node:  # If the node is None, its height is 0
                return 0

            # Recursively calculate the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # If any subtree is unbalanced or the current node is unbalanced, return -1
            if (
                left_height == -1  # Left subtree is unbalanced
                or right_height == -1  # Right subtree is unbalanced
                or abs(left_height - right_height) > 1  # Current node is unbalanced
            ):
                return -1

            # Return the height of the current node
            return 1 + max(left_height, right_height)

        # If the height function returns -1, the tree is unbalanced
        return height(root) != -1

    # Time: O(n)
    # Space: O(n)
    def by_iterative_dfs(self, root: Optional[TreeNode]) -> bool:
        # Initialize a stack with the root node and a visited flag set to False
        stack = [(root, False)]
        # Dictionary to store the depths of nodes
        depths = {}

        while stack:
            # Pop a node and its visited status from the stack
            node, visited = stack.pop()

            if node:
                if visited:
                    # If the node has been visited, calculate the depths of its subtrees
                    left_depth = depths.get(node.left, 0)  # Depth of the left subtree
                    right_depth = depths.get(
                        node.right, 0
                    )  # Depth of the right subtree

                    # If the difference in depths is greater than 1, the tree is unbalanced
                    if abs(left_depth - right_depth) > 1:
                        return False

                    # Store the depth of the current node
                    depths[node] = 1 + max(left_depth, right_depth)
                else:
                    # If the node has not been visited, push it back as visited
                    stack.append((node, True))
                    # Push the right and left children onto the stack
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        # If no imbalance is found, the tree is balanced
        return True

    def main(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        print(f"Input: root = {root}")
        print(f"Output (Brute Force): {self.by_brute_force(root)}")
        print(f"Output (Recursive DFS): {self.by_recursive_dfs(root)}")
        print(f"Output (Iterative DFS): {self.by_iterative_dfs(root)}")

        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
            TreeNode(2),
        )
        print(f"Input: root = {root}")
        print(f"Output (Brute Force): {self.by_brute_force(root)}")
        print(f"Output (Recursive DFS): {self.by_recursive_dfs(root)}")
        print(f"Output (Iterative DFS): {self.by_iterative_dfs(root)}")

        root = None
        print(f"Input: root = {root}")
        print(f"Output (Brute Force): {self.by_brute_force(root)}")
        print(f"Output (Recursive DFS): {self.by_recursive_dfs(root)}")
        print(f"Output (Iterative DFS): {self.by_iterative_dfs(root)}")


if __name__ == "__main__":
    IsBalanced().main()

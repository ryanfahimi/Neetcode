from typing import Optional

from TreeNode import TreeNode

# 124. Binary Tree Maximum Path Sum
# Hard

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.


# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:


# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


# Constraints:


# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000
class MaxPathSum:
    def by_brute_force(self, root: Optional[TreeNode]) -> int:
        # Helper function to calculate the path sum for a given node
        def find_path_sum(node):
            if not node:
                return 0

            # Recursively calculate the path sum for left and right subtrees
            left = find_path_sum(node.left)
            right = find_path_sum(node.right)

            # Calculate the path sum including the current node and the maximum of its subtrees
            path_sum = node.val + max(left, right)

            # Return the maximum path sum, ensuring it's non-negative
            return max(path_sum, 0)

        # Helper function to perform DFS and update the maximum path sum
        def find_max_path_sum(node):
            nonlocal max_path_sum
            if not node:
                return

            # Calculate the path sums for the left and right subtrees
            left = find_path_sum(node.left)
            right = find_path_sum(node.right)

            # Update the maximum path sum including the current node and its subtrees
            max_path_sum = max(max_path_sum, node.val + left + right)

            # Continue DFS traversal for left and right children
            find_max_path_sum(node.left)
            find_max_path_sum(node.right)

        # Initialize the maximum path sum to negative infinity
        max_path_sum = float("-inf")
        # Start the DFS traversal from the root node
        find_max_path_sum(root)
        # Return the maximum path sum found
        return int(max_path_sum)

    def by_dfs(self, root: Optional[TreeNode]) -> int:
        # Helper function to calculate the maximum path sum
        def find_max_path_sum(node):
            if not node:
                return 0

            # Recursively calculate the maximum path sum for left and right subtrees
            left = max(find_max_path_sum(node.left), 0)
            right = max(find_max_path_sum(node.right), 0)
            # Update the maximum path sum including the current node
            nonlocal max_path_sum
            max_path_sum = max(max_path_sum, left + right + node.val)
            # Return the maximum path sum including the current node
            return max(left, right) + node.val

        # Initialize the maximum path sum
        max_path_sum = float("-inf")
        # Start the recursion from the root node
        find_max_path_sum(root)
        # Return the maximum path sum found
        return int(max_path_sum)

    def main(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        print(f"root = {root}")
        print(f"Output (Brute Force): {self.by_brute_force(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")

        root = TreeNode(
            -10,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7)),
        )
        print(f"root = {root}")
        print(f"Output (Brute Force): {self.by_brute_force(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")


if __name__ == "__main__":
    MaxPathSum().main()

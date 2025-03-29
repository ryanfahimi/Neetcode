from typing import List, Optional

from TreeNode import TreeNode

# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]


# Constraints:


# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
class BuildTree:
    # Time: O(n)
    # Space: O(n)
    def by_dfs(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case
        if not preorder or not inorder:
            return None

        # Get the root node from the preorder list
        root = TreeNode(preorder[0])

        # Get the index of the root node in the inorder list
        root_index = inorder.index(preorder[0])

        # Build the left subtree
        root.left = self.by_dfs(preorder[1 : root_index + 1], inorder[:root_index])

        # Build the right subtree
        root.right = self.by_dfs(preorder[root_index + 1 :], inorder[root_index + 1 :])

        return root

    # Time: O(n)
    # Space: O(n)
    def by_optimal_dfs(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        # Create a dictionary to store the index of each node in the inorder list
        inorder_indexes = {val: index for index, val in enumerate(inorder)}

        # Initialize the preorder index
        preorder_index = 0

        # Helper function to build the tree
        def build(left, right):
            nonlocal preorder_index

            # Base case
            if left > right:
                return None

            # Get the root node from the preorder list
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1

            # Get the index of the root node in the inorder list
            root_index = inorder_indexes[root.val]

            # Build the left subtree
            root.left = build(left, root_index - 1)

            # Build the right subtree
            root.right = build(root_index + 1, right)

            return root

        return build(0, len(preorder) - 1)

    def main(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        print(f"Input: preorder = {preorder}, inorder = {inorder}")
        print(f"Output (DFS): {self.by_dfs(preorder, inorder)}")
        print(f"Output (Optimal DFS): {self.by_optimal_dfs(preorder, inorder)}")

        preorder = [-1]
        inorder = [-1]
        print(f"Input: preorder = {preorder}, inorder = {inorder}")
        print(f"Output (DFS): {self.by_dfs(preorder, inorder)}")
        print(f"Output (Optimal DFS): {self.by_optimal_dfs(preorder, inorder)}")


if __name__ == "__main__":
    BuildTree().main()

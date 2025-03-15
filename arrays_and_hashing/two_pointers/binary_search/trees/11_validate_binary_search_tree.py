from collections import deque
from typing import Optional

from TreeNode import TreeNode

# 98. Validate Binary Search Tree
# Medium

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


# Constraints:


# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1
class IsValidBST:
    # Time: O(n)
    # Space: O(n)
    def by_bfs(self, root: Optional[TreeNode]) -> bool:
        # Base case: if the tree is empty, return True
        if not root:
            return True

        # Initialize a queue with the root node and its boundaries
        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            # Pop the front node and its boundaries from the queue
            node, left, right = queue.popleft()

            # If the current node is None, continue to the next node
            if not node:
                continue

            # If the current node's value does not satisfy the BST property, return False
            if not left < node.val < right:
                return False

            # Append the left child with updated boundaries
            queue.append((node.left, left, node.val))
            # Append the right child with updated boundaries
            queue.append((node.right, node.val, right))

        return True

    # Time: O(n)
    # Space: O(n)
    def by_recursive_dfs(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left=float("-inf"), right=float("inf")):
            # Base case: if the node is None, it's a valid BST
            if not node:
                return True

            # If the current node's value does not satisfy the BST property, return False
            if not left < node.val < right:
                return False

            # Recursively validate the left and right subtrees
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        # Start the validation from the root with initial boundaries
        return valid(root)

    # Time: O(n)
    # Space: O(n)
    def by_iterative_dfs(self, root: Optional[TreeNode]) -> bool:
        # Initialize an empty stack and set the inorder value to negative infinity
        stack, inorder = [], float("-inf")

        # Iterate while there are nodes in the stack or the current node is not None
        while stack or root:
            # Traverse the left subtree
            while root:
                stack.append(root)
                root = root.left

            # Process the current node
            root = stack.pop()

            # If the current node's value is not greater than the inorder value, return False
            if root.val <= inorder:
                return False

            # Update the inorder value to the current node's value
            inorder = root.val
            # Traverse the right subtree
            root = root.right

        # If all nodes satisfy the BST property, return True
        return True

    def main(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (Recursive DFS): {self.by_recursive_dfs(root)}")
        print(f"Output (Iterative DFS): {self.by_iterative_dfs(root)}")

        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (Recursive DFS): {self.by_recursive_dfs(root)}")
        print(f"Output (Iterative DFS): {self.by_iterative_dfs(root)}")


if __name__ == "__main__":
    IsValidBST().main()

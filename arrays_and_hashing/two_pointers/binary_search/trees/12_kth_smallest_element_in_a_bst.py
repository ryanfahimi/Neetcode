from typing import Optional

from TreeNode import TreeNode

# 230. Kth Smallest Element in a BST
# Medium

# Hint
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104


# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
class KthSmallest:
    # Time: O(n)
    # Space: O(n)
    def by_brute_force(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(node):
            if not node:
                return []

            # Traverse the left subtree, then visit the node, and finally traverse the right subtree
            return traverse(node.left) + [node.val] + traverse(node.right)

        # Perform inorder traversal and get the k-1 element (1-indexed to 0-indexed)
        return traverse(root)[k - 1]

    # Time: O(n)
    # Space: O(n)
    def by_recursive_dfs(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        result = 0

        def traverse(node):
            nonlocal counter, result

            if not node:
                return

            # Traverse the left subtree
            traverse(node.left)

            # Visit the node
            counter -= 1
            if counter == 0:
                result = node.val
                return

            # Traverse the right subtree
            traverse(node.right)

        traverse(root)
        return result

    # Time: O(n)
    # Space: O(n)
    def by_iterative_dfs(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        counter = k
        current = root

        # Iterate until there are no nodes left to process
        while stack or current:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process the node
            current = stack.pop()
            counter -= 1
            if counter == 0:
                return current.val

            # Go to the right node
            current = current.right

    def main(self):
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        k = 1
        print(f"Input: root = {root}, k = {k}")
        print(f"Output (Brute Force): {self.by_brute_force(root, k)}")
        print(f"Output (Recursive DFS): {self.by_recursive_dfs(root, k)}")
        print(f"Output (Iterative DFS): {self.by_iterative_dfs(root, k)}")

        root = TreeNode(
            5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)
        )
        k = 3
        print(f"Input: root = {root}, k = {k}")
        print(f"Output (Brute Force): {self.by_brute_force(root, k)}")
        print(f"Output (Recursive DFS): {self.by_recursive_dfs(root, k)}")
        print(f"Output (Iterative DFS): {self.by_iterative_dfs(root, k)}")


if __name__ == "__main__":
    KthSmallest().main()

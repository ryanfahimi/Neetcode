from typing import Optional

from TreeNode import TreeNode

# 235. Lowest Common Ancestor of a Binary Search Tree
# Medium

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2


# Constraints:


# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.
class LowestCommonAncestor:
    # Time: O(h)
    # Space: O(h)
    def by_recursive(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root or not p or not q:
            return None

        # If both p and q are less than the current node's value, the LCA is in the left subtree
        if p.val < root.val and q.val < root.val:
            return self.by_recursive(root.left, p, q)

        # If both p and q are greater than the current node's value, the LCA is in the right subtree
        if p.val > root.val and q.val > root.val:
            return self.by_recursive(root.right, p, q)

        # If p and q are on either side of the current node's value, the current node is the LCA
        return root

    # Time: O(h)
    # Space: O(1)
    def by_iterative(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root or not p or not q:
            return None

        while root:
            # If both p and q are less than the current node's value, the LCA is in the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left

            # If both p and q are greater than the current node's value, the LCA is in the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # If p and q are on either side of the current node's value, the current node is the LCA
            else:
                return root

    def main(self):
        root = TreeNode(
            6,
            TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
            TreeNode(8, TreeNode(7), TreeNode(9)),
        )
        p = TreeNode(2)
        q = TreeNode(8)
        print(f"Input: root = {root}, p = {p}, q = {q}")
        print(f"Output (Recursive): {self.by_recursive(root, p, q)}")
        print(f"Output (Iterative): {self.by_iterative(root, p, q)}")

        q = TreeNode(4)
        print(f"Input: root = {root}, p = {p}, q = {q}")
        print(f"Output (Recursive): {self.by_recursive(root, p, q)}")
        print(f"Output (Iterative): {self.by_iterative(root, p, q)}")

        root = TreeNode(2, TreeNode(1))
        q = TreeNode(1)
        print(f"Input: root = {root}, p = {p}, q = {q}")
        print(f"Output (Recursive): {self.by_recursive(root, p, q)}")
        print(f"Output (Iterative): {self.by_iterative(root, p, q)}")


if __name__ == "__main__":
    LowestCommonAncestor().main()

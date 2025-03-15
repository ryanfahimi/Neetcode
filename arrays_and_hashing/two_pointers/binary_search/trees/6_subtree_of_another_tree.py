from typing import Optional

from TreeNode import TreeNode

# 572. Subtree of Another Tree
# Easy

# Hint
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false


# Constraints:


# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104
class IsSubtree:
    # Time: O(n * m)
    # Space: O(n)
    def by_dfs(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # Base case: if both trees are empty
            if not p and not q:
                return True

            # Check if both nodes are not None, their values are equal, and recursively check their children
            return (
                p is not None
                and q is not None
                and p.val == q.val
                and is_same_tree(p.left, q.left)
                and is_same_tree(p.right, q.right)
            )

        # Base case: if the subRoot is None, return True
        if sub_root is None:
            return True

        # Base case: if the root is None, return False
        if not root:
            return False

        # Check if the current node is the same as the subRoot
        if is_same_tree(root, sub_root):
            return True

        # Recursively check the left and right subtrees
        return self.by_dfs(root.left, sub_root) or self.by_dfs(root.right, sub_root)

    def by_serializing(
        self, root: Optional[TreeNode], sub_root: Optional[TreeNode]
    ) -> bool:
        def serialize(node):
            if not node:
                return "null"

            return f"{node.val},{serialize(node.left)},{serialize(node.right)}"

        return serialize(sub_root) in serialize(root)

    def main(self):
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
        print(f"Input: root = {root}, subRoot = {sub_root}")
        print(f"Output (DFS): {self.by_dfs(root, sub_root)}")
        print(f"Output (Serializing): {self.by_serializing(root, sub_root)}")

        root = TreeNode(
            3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5)
        )
        sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
        print(f"Input: root = {root}, subRoot = {sub_root}")
        print(f"Output (DFS): {self.by_dfs(root, sub_root)}")
        print(f"Output (Serializing): {self.by_serializing(root, sub_root)}")


if __name__ == "__main__":
    IsSubtree().main()

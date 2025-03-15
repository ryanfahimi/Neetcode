from collections import deque

from TreeNode import TreeNode

# 1448. Count Good Nodes in Binary Tree
# Medium

# Hint
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.


# Example 1:


# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# Example 2:


# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# Example 3:

# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.


# Constraints:


# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].
class GoodNodes:
    # Time: O(n)
    # Space: O(n)
    def by_bfs(self, root: TreeNode) -> int:
        # Base case
        if not root:
            return 0

        # Initialize the count of good nodes
        counter = 0

        # Initialize a queue for BFS and add the root node along with the maximum value in the path
        queue = deque([(root, root.val)])

        # Loop until the queue is empty
        while queue:
            # Process all nodes at the current level
            for _ in range(len(queue)):
                node, max_val = queue.popleft()

                # If the current node's value is greater than or equal to the maximum value in the path
                if node.val >= max_val:
                    # Increment the count of good nodes
                    counter += 1
                    # Update the maximum value in the path
                    max_val = node.val

                # Add left child to the queue if it exists
                if node.left:
                    queue.append((node.left, max_val))
                # Add right child to the queue if it exists
                if node.right:
                    queue.append((node.right, max_val))

        return counter

    # Time: O(n)
    # Space: O(n)
    def by_dfs(self, root: TreeNode) -> int:
        def count(node, max_val):
            # Base case
            if not node:
                return 0

            # Initialize the count of good nodes
            counter = 0

            # If the current node's value is greater than or equal to the maximum value in the path
            if node.val >= max_val:
                # Increment the count of good nodes
                counter += 1
                # Update the maximum value in the path
                max_val = node.val

            # Recursively process the left and right children
            counter += count(node.left, max_val)
            counter += count(node.right, max_val)

            return counter

        # Start the DFS traversal from the root node with the minimum value
        return count(root, float("-inf"))

    def main(self):
        root = TreeNode(
            3,
            TreeNode(1, TreeNode(3)),
            TreeNode(4, None, TreeNode(1, None, TreeNode(5))),
        )
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")

        root = TreeNode(3, TreeNode(3, None, TreeNode(4)), TreeNode(2))
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")

        root = TreeNode(1)
        print(f"Input: root = {root}")
        print(f"Output (BFS): {self.by_bfs(root)}")
        print(f"Output (DFS): {self.by_dfs(root)}")


if __name__ == "__main__":
    GoodNodes().main()

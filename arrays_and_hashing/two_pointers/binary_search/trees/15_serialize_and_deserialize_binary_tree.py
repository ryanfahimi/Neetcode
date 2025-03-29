from TreeNode import TreeNode

# 297. Serialize and Deserialize Binary Tree
# Hard

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.


# Example 1:


# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []


# Constraints:


# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000
class Codec:
    # Time: O(n)
    # Space: O(n)
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        return (
            f"{root.val} {root.left if root.left else "/"} {root.right if root.right else "/"}"
            if root
            else "/"
        )

    # Time: O(n)
    # Space: O(n)
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split()  # Split the serialized string into a list of values
        # Initialize an index to keep track of the current position in the list
        index = 0

        def traverse(val):
            nonlocal index  # Allow modification of the index variable in the outer scope
            index += 1  # Move to the next value in the list
            if val == "/":
                # If the value is "/", it represents a null node
                return None

            # Create a new TreeNode with the current value
            node = TreeNode(val)
            # Recursively construct the left subtree
            node.left = traverse(data[index])
            # Recursively construct the right subtree
            node.right = traverse(data[index])

            return node  # Return the constructed node

        # Start the traversal with the first value in the list
        return traverse(data[index])

    # Your Codec object will be instantiated and called as such:
    # ser = Codec()
    # deser = Codec()
    # ans = deser.deserialize(ser.serialize(root))
    def main(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        codec = Codec()
        print("Command: Codec()")
        print(f"Input: root = {root}")
        print("Command: codec.serialize(root)")
        print(f"Output: {codec.serialize(root)}")
        print("Command: codec.deserialize(codec.serialize(root))")
        print(f"Output: {codec.deserialize(codec.serialize(root))}")

        root = None
        print(f"Input: root = {root}")
        print("Command: codec.serialize(root)")
        print(f"Output: serialized_data = {codec.serialize(root)}")
        print("Command: codec.deserialize(codec.serialize(root))")
        print(f"Output: {codec.deserialize(codec.serialize(root))}")


if __name__ == "__main__":
    Codec().main()

from typing import List

# 22. Generate Parentheses
# Medium

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8


class Solution:
    # Time: O(4^n / sqrt(n))
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize an empty stack to store the parentheses
        stack = []
        # Initialize the result array
        result = []

        # Helper function to generate the parentheses
        def generate(left, right):
            # Base case: if the number of left and right parentheses is equal to n
            if left == n and right == n:
                # Append the parentheses to the result array
                result.append("".join(stack))
                return

            # If the number of left parentheses is less than n
            if left < n:
                # Push a left parenthesis to the stack
                stack.append("(")
                # Recursively generate the next parentheses
                generate(left + 1, right)
                # Pop the left parenthesis from the stack
                stack.pop()

            # If the number of right parentheses is less than the number of left parentheses
            if right < left:
                # Push a right parenthesis to the stack
                stack.append(")")
                # Recursively generate the next parentheses
                generate(left, right + 1)
                # Pop the right parenthesis from the stack
                stack.pop()

        # Generate the parentheses starting with a left parenthesis
        generate(0, 0)

        return result

    def main(self):
        n = 3
        print(f"Input: n = {n}")
        print(f"Output: {self.generateParenthesis(n)}")

        n = 1
        print(f"Input: n = {n}")
        print(f"Output: {self.generateParenthesis(n)}")


if __name__ == "__main__":
    Solution().main()

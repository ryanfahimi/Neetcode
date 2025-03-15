from typing import List

# 150. Evaluate Reverse Polish Notation
# Medium

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.


# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


# Constraints:


# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


class Solution:
    # Time: O(n)
    # Space: O(n)
    def eval_rpn(self, tokens: List[str]) -> int:
        # Initialize an empty stack to store operands
        stack = []

        # Define a set of valid operators
        operators = set("+-*/")

        # Iterate through each token in the input list
        for token in tokens:
            # If the token is an operator, pop the top two elements from the stack
            if token in operators:
                second, first = stack.pop(), stack.pop()

                # Perform the corresponding operation and push the result back onto the stack
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    # For division, convert the result to an integer to truncate towards zero
                    stack.append(int(first / second))
            else:
                # If the token is an operand, convert it to an integer and push it onto the stack
                stack.append(int(token))

        # The final result will be the only element left in the stack
        return stack[0]

    def main(self):
        tokens = ["2", "1", "+", "3", "*"]
        print(f"Input: tokens = {tokens}")
        print(f"Output: {self.eval_rpn(tokens)}")

        tokens = ["4", "13", "5", "/", "+"]
        print(f"Input: tokens = {tokens}")
        print(f"Output: {self.eval_rpn(tokens)}")

        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        print(f"Input: tokens = {tokens}")
        print(f"Output: {self.eval_rpn(tokens)}")


if __name__ == "__main__":
    Solution().main()

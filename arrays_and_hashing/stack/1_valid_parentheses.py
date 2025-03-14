# 20. Valid Parentheses
# Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


# Constraints:


# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
class IsValid:
    # Time: O(n)
    # Space: O(n)
    def by_brute_force(self, s: str) -> bool:
        # Initialize an empty stack
        stack = []
        for c in s:
            # If the character is an opening bracket, push it to the stack
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                # If the stack is empty, it means there's no corresponding opening bracket for the current closing bracket
                if not stack:
                    return False
                # If the top of the stack is not the corresponding opening bracket for the current closing bracket, return False
                if c == ")" and stack[-1] != "(":
                    return False
                if c == "]" and stack[-1] != "[":
                    return False
                if c == "}" and stack[-1] != "{":
                    return False
                # If the top of the stack is the corresponding opening bracket for the current closing bracket, pop it from the stack
                stack.pop()
        # If the stack is empty at the end, it means all brackets are correctly paired and nested
        return not stack

    # Time: O(n)
    # Space: O(n)
    def by_hash_map(self, s: str) -> bool:
        # Initialize an empty stack
        stack = []
        # Define a hash map where the keys are the closing brackets and the values are the corresponding opening brackets
        parentheses = {")": "(", "]": "[", "}": "{"}
        for c in s:
            # If the character is a closing bracket
            if c in parentheses:
                # If the stack is empty or the top of the stack is not the corresponding opening bracket, return False
                if not stack or stack[-1] != parentheses[c]:
                    return False
                # If the top of the stack is the corresponding opening bracket, pop it from the stack
                stack.pop()
            else:
                # If the character is an opening bracket, push it to the stack
                stack.append(c)
        # If the stack is empty at the end, it means all brackets are correctly paired and nested
        return not stack

    def main(self):
        s = "()"
        print(f"Input: {s}")
        print(f"Brute Force Output: {self.by_brute_force(s)}")
        print(f"Hash Map Output: {self.by_hash_map(s)}")

        s = "()[]{}"
        print(f"Input: {s}")
        print(f"Brute Force Output: {self.by_brute_force(s)}")
        print(f"Hash Map Output: {self.by_hash_map(s)}")

        s = "(]"
        print(f"Input: {s}")
        print(f"Brute Force Output: {self.by_brute_force(s)}")
        print(f"Hash Map Output: {self.by_hash_map(s)}")


if __name__ == "__main__":
    IsValid().main()

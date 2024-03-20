# 155. Min Stack
# Medium

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int get_min() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


# Example 1:

# Input
# ["MinStack","push","push","push","get_min","pop","top","get_min"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack min_stack = new MinStack();
# min_stack.push(-2);
# min_stack.push(0);
# min_stack.push(-3);
# min_stack.get_min(); // return -3
# min_stack.pop();
# min_stack.top();    // return 0
# min_stack.get_min(); // return -2


# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and get_min operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and get_min.


class MinStack:
    # Time: O(1)
    def __init__(self):
        # Main stack to hold all elements
        self.stack = []
        # Stack to hold minimum elements
        self.min_stack = []

    # Time: O(1)
    def push(self, val: int) -> None:
        # Push the element val onto the main stack
        self.stack.append(val)
        # If min_stack is not empty, compare the element val with the top of min_stack
        # assign the smaller value to val
        if self.min_stack:
            val = min(val, self.min_stack[-1])
        # Push the element val onto min_stack
        self.min_stack.append(val)

    # Time: O(1)
    def pop(self) -> None:
        # Remove the top element from the main stack
        self.stack.pop()
        # Remove the top element from min_stack
        self.min_stack.pop()

    # Time: O(1)
    def top(self) -> int:
        # Return the top element from the main stack
        return self.stack[-1]

    # Time: O(1)
    def get_min(self) -> int:
        # Retrieves the minimum element in the stack.
        # Return the top element from min_stack
        return self.min_stack[-1]

    def main(self):
        print("Command: MinStack()")
        min_stack = MinStack()
        print("Command: push(-2)")
        min_stack.push(-2)
        print("Command: push(0)")
        min_stack.push(0)
        print("Command: push(-3)")
        min_stack.push(-3)
        print("Command: get_min()")
        print("Output:", min_stack.get_min())
        print("Command: pop()")
        min_stack.pop()
        print("Command: top()")
        print("Output:", min_stack.top())
        print("Command: get_min()")
        print("Output:", min_stack.get_min())


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.main()

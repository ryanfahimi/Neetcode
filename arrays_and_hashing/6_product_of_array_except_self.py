from typing import List

# 238. Product of Array Except Self
# Medium

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# Constraints:

# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


class ProductExceptSelf:
    # Time: O(n)
    def by_arrays(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # Create a three lists of size n
        output = [1] * length
        left = [1] * length
        right = [1] * length
        # Iterate through the list
        for i in range(1, length):
            # Multiply the previous element by the current element
            left[i] = left[i - 1] * nums[i - 1]
        # Iterate through the list in reverse
        for i in reversed(range(length - 1)):
            # Multiply the previous element by the current element
            right[i] = right[i + 1] * nums[i + 1]
        # Iterate through the list
        for i in range(length):
            # Multiply the left element by the right element
            output[i] = left[i] * right[i]
        return output

    # Time: O(n)
    def by_array(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # Create a list of size n
        output = [1] * length
        # Iterate through the list
        for i in range(1, length):
            # Multiply the previous element by the current element
            output[i] = output[i - 1] * nums[i - 1]
        # Create a variable to keep track of the product of the elements to the right of the current element
        right = 1
        # Iterate through the list in reverse
        for i in reversed(range(length)):
            # Multiply the current element by the product of the elements to the right of the current element
            output[i] *= right
            # Multiply the product of the elements to the right of the current element by the current element
            right *= nums[i]
        return output

    def main(self):
        nums = [1, 2, 3, 4]
        print(f"Input: nums = {nums}")
        print(f"Arrays Output: {self.by_arrays(nums)}")
        print(f"Array Output: {self.by_array(nums)}")

        nums = [-1, 1, 0, -3, 3]
        print(f"Input: nums = {nums}")
        print(f"Arrays Output: {self.by_arrays(nums)}")
        print(f"Array Output: {self.by_array(nums)}")


if __name__ == "__main__":
    ProductExceptSelf().main()

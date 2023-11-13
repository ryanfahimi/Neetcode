from typing import List
import timeit


class productExceptSelf:
    # Time: O(n^2)
    # Space: O(1)
    def brute_force(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # Create a list of size n
        output = [1] * length
        # Iterate through the list
        for i in range(length):
            # Iterate through the list
            for j in range(length):
                # If the indices are not equal
                if i != j:
                    # Multiply the current element by the current element
                    output[i] *= nums[j]
        return output

    # Time: O(n)
    # Space: O(n)
    def arrays(self, nums: List[int]) -> List[int]:
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
    # Space: O(1)
    def array(self, nums: List[int]) -> List[int]:
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
        funcs = [self.brute_force, self.arrays, self.array]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(nums))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    productExceptSelf().main()

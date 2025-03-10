from typing import List

# 74. Search a 2D Matrix
# Medium

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


# Constraints:


# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104
class SearchMatrix:
    # Time: O(log(m) + log(n))
    def by_two_passes(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # First pass: find the row
        top, bottom = 0, m - 1
        while top <= bottom:
            row = top + (bottom - top) // 2
            # If the target is less than the first element of the row, search in the top half
            if target < matrix[row][0]:
                bottom = row - 1
            # If the target is greater than the last element of the row, search in the bottom half
            elif target > matrix[row][n - 1]:
                top = row + 1
            # If the target is in the row, break the loop
            else:
                break

        # If the target is not in the matrix, return False
        if top > bottom:
            return False

        # Second pass: find the column
        left, right = 0, n - 1
        while left <= right:
            column = left + (right - left) // 2
            # If the middle element is less than the target, search in the right half
            if matrix[row][column] < target:
                left = column + 1
            # If the middle element is greater than the target, search in the left half
            elif matrix[row][column] > target:
                right = column - 1
            # If the middle element is the target, return True
            else:
                return True

        return False

    # Time: O(log(m * n))
    def by_one_pass(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            # Calculate the row and column of the middle element
            row = mid // n
            column = mid % n
            mid_element = matrix[row][column]

            # If the middle element is the target, return True
            if mid_element == target:
                return True
            # If the middle element is less than the target, search in the right half
            elif mid_element < target:
                left = mid + 1
            # If the middle element is greater than the target, search in the left half
            else:
                right = mid - 1

        return False

    def main(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        print(f"Input: matrix = {matrix}, target = {target}")
        print(f"Two Passes Output: {self.by_two_passes(matrix, target)}")
        print(f"One Pass Output: {self.by_one_pass(matrix, target)}")

        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        print(f"Input: matrix = {matrix}, target = {target}")
        print(f"Two Passes Output: {self.by_two_passes(matrix, target)}")
        print(f"One Pass Output: {self.by_one_pass(matrix, target)}")


if __name__ == "__main__":
    SearchMatrix().main()

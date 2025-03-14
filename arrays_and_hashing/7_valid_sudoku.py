from typing import List

# 36. Valid Sudoku
# Medium

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


# Example 1:


# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:

# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


class IsValidSudoku:
    # Time: O(n^2)
    # Space: O(n)
    def by_boolean_arrays(self, board: List[List[str]]) -> bool:
        # Create a list of 9 lists of 9 False values
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]
        # Iterate through the board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != ".":
                    index = int(cell) - 1
                    box_index = (i // 3) * 3 + j // 3
                    # If the number is in the row, column, or box
                    if rows[i][index] or cols[j][index] or boxes[box_index][index]:
                        return False
                    # Add the number to the row, column, and box
                    rows[i][index] = True
                    cols[j][index] = True
                    boxes[box_index][index] = True
        return True

    # Time: O(n^2)
    # Space: O(n^2)
    def by_sets(self, board: List[List[str]]) -> bool:
        # Create a set for each row, column, and box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        # Iterate through the board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != ".":
                    box_index = (i // 3) * 3 + j // 3
                    # If the number is in the row, column, or box
                    if cell in rows[i] or cell in cols[j] or cell in boxes[box_index]:
                        return False
                    # Add the number to the row, column, and box
                    rows[i].add(cell)
                    cols[j].add(cell)
                    boxes[box_index].add(cell)
        return True

    def main(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        print(f"Input: board = ")
        for row in board:
            print(row)
        print(f"Boolean Arrays Output: {self.by_boolean_arrays(board)}")
        print(f"Sets Output: {self.by_sets(board)}")

        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        print(f"Input: board = ")
        for row in board:
            print(row)
        print(f"Boolean Arrays Output: {self.by_boolean_arrays(board)}")
        print(f"Sets Output: {self.by_sets(board)}")


if __name__ == "__main__":
    IsValidSudoku().main()

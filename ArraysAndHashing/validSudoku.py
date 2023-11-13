from typing import List
import timeit


class validSudoku:
    # Time: O(1)
    # Space: O(1)
    def on_the_fly(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != ".":
                    for k in range(9):
                        if k != i and cell == board[k][j]:
                            return False
                        if k != j and cell == board[i][k]:
                            return False
                        box_row = (i // 3) * 3 + k // 3
                        box_col = (j // 3) * 3 + k % 3
                        if (box_row != i or box_col != j) and cell == board[box_row][
                            box_col
                        ]:
                            return False
        return True

    # Time: O(1)
    # Space: O(1)
    def boolean_arrays(self, board: List[List[str]]) -> bool:
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

    # Time: O(1)
    # Space: O(n)
    def hash_set(self, board: List[List[str]]) -> bool:
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
        funcs = [self.on_the_fly, self.boolean_arrays, self.hash_set]
        for func in funcs:
            start_time = timeit.default_timer()
            print(func(board))
            end_time = timeit.default_timer()
            print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds.")


if __name__ == "__main__":
    validSudoku().main()

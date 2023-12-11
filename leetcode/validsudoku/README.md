# Intuition
We're going to create a couple functions here, they allow us to extend this code in future if we need similar functionality. All we're doing is checking three things: rows, columns, and squares. We'll check rows and columns by iterating through the board and checking each row and column. We'll check squares by iterating through the board and checking each square.

# Approach
1. Check rows
    1. Iterate through each row
    2. Check each row
        1. Create a set
        2. Iterate through each element in the row
        3. If the element is a period, continue
        4. If the element is in the set, return false
        5. Else, add the element to the set
    3. Return true
 2. Check columns
    1. Use the same logic as checking rows, but transpose the board first
 3. Check squares
    1. Iterate through each square
        1. Create a set
        2. Iterate through each element in the square
        3. If the element is a period, continue
        4. If the element is in the set, return false
        5. Else, add the element to the set
    2. Return true

# Complexity
- Time complexity: $$O(n^2)$$
  - [[1..9]..[1..9]] is $$n^2$$
  - The case is no worse for checking squares

- Space complexity: $$O(n)$$
  - We're storing a set of size $$n$$ for each row, column, and square

# Code
```
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.checkLinear(board, True):
            return False
        if not self.checkLinear(board, False):
            return False
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                if not self.checkSquare(board, 3, i, j):
                    return False
        return True

    def checkLinear(self, board: List[List[str]], rowsNotColumns: bool) -> bool:
        if rowsNotColumns:
            for i in range(len(board)):
                s = set()
                for j in range(len(board[i])):
                    print(s)
                    if board[i][j] == '.':
                        continue
                    elif board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
            return True
        elif not rowsNotColumns:
            for i in range(len(board)):
                s = set()
                for j in range(len(board[i])):
                    print(s)
                    if board[j][i] == '.':
                        continue
                    elif board[j][i] in s:
                        return False
                    else:
                        s.add(board[j][i])
            return True

    def checkSquare(self, 
            board: List[List[str]], span: int,
            startingRow: int, startingColumn: int) -> bool:
        s = set()
        for i in range(startingRow, startingRow + span):
            for j in range(startingColumn, startingColumn + span):
                if board[i][j] == '.':
                        continue
                elif board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
        return True
```
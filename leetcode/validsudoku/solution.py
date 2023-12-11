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
            s = set()
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
            return True
        elif not rowsNotColumns:
            s = set()
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[j][i] in s:
                        return False
                    else:
                        s.add(board[j][i])
            return True

    def checkSquare(self, 
            board: List[List[str]], range: int,
            startingRow: int, startingColumn: int) -> bool:
        s = set()
        for i in range(startingRow, startingRow + range):
            for j in range(startingColumn, startingColumn + range):
                if board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
        return True
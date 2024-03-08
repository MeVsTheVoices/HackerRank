import itertools
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> List[List[str]]:
        """
        Do not return anything, modify board in-place instead.
        """
        

    def calculatePossibilities(self, board):
        possibilities = []
        for i in range(len(board)):
            possibilities.append(list())
            for j in range(len(board[i])):
                possibilities[i].append(list())
                if board[i][j] == ".":
                    possibilities[i][j] = [self.checkValid(board, i, j, str(number)) for number in range(1, 10)]
        return possibilities

        
    def checkColumnElement(self, board, row, column, number):
        m = range(0, row)
        n = range(row + 1, 9)
        uninclusive = list(m) + list(n)
        return any([board[i][column] == number for i in uninclusive])
    
    def checkRowElement(self, board, row, column, number):
        m = range(0, column)
        n = range(column + 1, 9)
        uninclusive = list(m) + list(n)
        return any([board[row][i] == number for i in uninclusive])
    
    def getSquare(self, row, column):
        if row in [0, 3, 6]:
            row += 1
        elif row in [2, 5, 8]:
            row -= 1
        if column in [0, 3, 6]:
            column += 1
        elif column in [2, 5, 8]:
            column -= 1
        return row, column


    def checkSquare(self, board, row, column, number):
        squareRow, squareColumn = self.getSquare(row, column)
        for i in range(squareRow - 1, squareRow + 1):
            for j in range(squareColumn - 1, squareColumn + 1):
                if number == board[i][j] and ((i != row) or (j != column)):
                    return True
        return False
    
    def checkValid(self, board, row, column, number):
        return not (self.checkColumnElement(board, row, column, number) or self.checkRowElement(board, row, column, number) or self.checkSquare(board, row, column, number))
    
    def checkValidAll(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    if not self.checkValid(board, i, j, board[i][j]):
                        return False
        return True
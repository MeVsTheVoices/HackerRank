import itertools
import unittest
from leetcode.sudokusolver.solution import Solution

class RemoveElementTest(unittest.TestCase):
    def testCheckColumnElement(self):
        # Make sure that the board we're given is valid
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    checkColumnElement = Solution().checkColumnElement(board, i, j, board[i][j])
                    self.assertFalse(checkColumnElement)

        board = [[".",".",".",".",".",".",".",".","2"],[".",".",".",".",".",".","6",".","."],[".",".","1","4",".",".","8",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".","3",".",".",".","."],["5",".","8","6",".",".",".",".","."],[".","9",".",".",".",".","4",".","."],[".",".",".",".","5",".",".",".","."]]
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    checkColumnElement = Solution().checkColumnElement(board, i, j, board[i][j])
                    self.assertFalse(checkColumnElement)

    def testCheckRowElement(self):
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    checkRowElement = Solution().checkRowElement(board, i, j, board[i][j])
                    self.assertFalse(checkRowElement)

        board = [[".",".",".",".",".",".",".",".","2"],[".",".",".",".",".",".","6",".","."],[".",".","1","4",".",".","8",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".","3",".",".",".","."],["5",".","8","6",".",".",".",".","."],[".","9",".",".",".",".","4",".","."],[".",".",".",".","5",".",".",".","."]]
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    checkRowElement = Solution().checkRowElement(board, i, j, board[i][j])
                    self.assertFalse(checkRowElement)


    def testGetSquare(self):
        # Check that we round down or up to the center of 3x3 squares
        i, j = 0, 0
        squareRow, squareColumn = Solution().getSquare(i, j)
        self.assertEqual(squareRow, 1)
        self.assertEqual(squareColumn, 1)

        i, j = 8, 8
        squareRow, squareColumn = Solution().getSquare(i, j)
        self.assertEqual(squareRow, 7)
        self.assertEqual(squareColumn, 7)

    def testCheckSquare(self):
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    checkSquare = Solution().checkSquare(board, i, j, board[i][j])
                    self.assertFalse(checkSquare)

    def testCheckValid(self):
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    checkValid = Solution().checkValid(board, i, j, board[i][j])
                    self.assertTrue(checkValid)

    def testSolveSudoku(self):
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        sol = Solution()
        sol.solveSudoku(board)

        # Check that the board is valid
        expected = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
        self.assertEqual(board, expected)

        #for i in range(0, 9):
        #    for j in range(0, 9):
        #        if board[i][j] != ".":
        #            print(sol.checkColumnElement(board, i, j, board[i][j]))
        #            print(sol.checkRowElement(board, i, j, board[i][j]))
        #            print(sol.checkSquare(board, i, j, board[i][j]))

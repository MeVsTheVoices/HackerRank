from itertools import pairwise
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return sum(
            [self.calculateSingleList(grid[i]) for i in range(len(grid))] +
            [self.calculateSingleList(self.transpose(grid)[i]) for i in range(len(grid[0]))]
        )

    def calculateSingleList(self, list: List[int]) -> int:
        fixedList = [0] + list + [0]
        edgeCount = 0
        for x, y in pairwise(fixedList):
            if x != y:
                edgeCount += 1
        return edgeCount

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [ [ matrix[j][i] for j in range(len(matrix)) ] for i in range(len(matrix[0])) ]
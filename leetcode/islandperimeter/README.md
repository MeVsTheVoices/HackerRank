# Intuition
1. View it as a plane from above
    1. From here, any transition is an edge
    2. We add whitespace on the edges to include transitions from where black would go to white

# Approach
We just wrote transpose, so, gonna include it here, we do the same thing twice, count the number of edges in each row, then do the same on the transpose of the matrix.

# Complexity
- Time complexity: O(n)

- Space complexity: O(1)

# Code
```python3 []
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
```
# Intuition
Read it backwards

# Approach
Read by column then row

# Complexity
- Time complexity: O(n^2)

- Space complexity: O(1)

# Code
```python3 []
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [ [ matrix[j][i] for j in range(len(matrix)) ] for i in range(len(matrix[0])) ]
```
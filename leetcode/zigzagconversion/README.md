# Intuition
We're converting a string in to a matrix of characters in a zigzag method, then reading the characters off the matrix in order.

# Approach
    - Create a matrix of characters
    - Iterate through the string, adding characters to the matrix in a zigzag pattern
    - Read the characters off the matrix in order

# Complexity
- Time complexity: O(n)

- Space complexity: O(n^2)

# Code
```
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = [[] for row in range(numRows)]
        goingDown = True
        index = 0
        for character in s:
            if goingDown and index == numRows - 1:
                goingDown = False
            elif not goingDown and index == 0:
                goingDown = True
            res[index].append(character)
            if goingDown:
                index += 1
            else:
                index -= 1
        
        for row in range(len(res)):
            res[row] = ''.join(res[row])
        
        return ''.join(res)

```
# Intuition
This is the simplest approach I can imagine, we deal with the base case, then iterate through rows.

# Approach
- Start with the rows
- With each row find the minimum
- Then check the column it's in
- Only preserve values of the minimum of the row if it is the maximum of the column

# Complexity
- Time complexity: O(n^2)

- Space complexity: O(1)

# Code
```
class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        List<Integer> luckyNumbers = new LinkedList<>();
        if (matrix.length == 0)
            return luckyNumbers;

        for (int i = 0; i < matrix.length; i++) {
            int minIndex = 0;
            boolean wasMaxInColumn = true;
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] < matrix[i][minIndex])
                    minIndex = j;
            }
            for (int k = 0; k < matrix.length; k++) {
                if (matrix[k][minIndex] > matrix[i][minIndex])
                    wasMaxInColumn = false;
            }
            if (wasMaxInColumn)
                luckyNumbers.add(matrix[i][minIndex]);
        }
        return luckyNumbers;
    }
}
```
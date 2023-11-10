package leetcode.luckynumbersinmatrix;

import java.util.LinkedList;
import java.util.List;

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
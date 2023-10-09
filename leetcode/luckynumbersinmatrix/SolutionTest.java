package leetcode.luckynumbersinmatrix;

import org.junit.Test;

import org.junit.Assert;

public class SolutionTest {
    @Test
    public void testLuckyNumbers() {
        Solution solution = new Solution();

        int[][] matrix1 = {{3, 7, 8}, {9, 11, 13}, {15, 16, 17}};
        int[] expected1 = {15};
        int[] result1 = solution.luckyNumbers(matrix1).stream().mapToInt(i -> i).toArray();
        Assert.assertArrayEquals(expected1, result1);

        int[][] matrix2 = {{1, 10, 4, 2}, {9, 3, 8, 7}, {15, 16, 17, 12}};
        int[] expected2 = {12};
        int[] result2 = solution.luckyNumbers(matrix2).stream().mapToInt(i -> i).toArray();
        Assert.assertArrayEquals(expected2, result2);

        int[][] matrix3 = {{7, 8}, {1, 2}};
        int[] expected3 = {7};
        int[] result3 = solution.luckyNumbers(matrix3).stream().mapToInt(i -> i).toArray();
        Assert.assertArrayEquals(expected3, result3);
    }
}

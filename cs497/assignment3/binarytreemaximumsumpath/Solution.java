package cs497.assignment3.binarytreemaximumsumpath;

import cs497.assignment3.TreeNode;

import java.util.*;

class Solution {
    private int currentMax = Integer.MIN_VALUE;
    private Map<TreeNode, Integer> memo = new HashMap<>();
    
    public int maxPathSum(TreeNode root) {
        currentMax = Integer.MIN_VALUE;
        maxPathSumHelper(root);
        return currentMax;
    }

    private int maxPathSumHelper(TreeNode start) {
        if (start == null)
            return 0;

        if (memo.containsKey(start))
            return memo.get(start);

        int left = maxPathSumHelper(start.left);
        int right = maxPathSumHelper(start.right);

        int mostIfSplit = left + right + start.val;
        int mostIfNotSplit = Math.max(left, right) + start.val;

        int result = Math.max(mostIfSplit, Math.max(mostIfNotSplit, start.val));
        currentMax = Math.max(result, currentMax);
        memo.put(start, result);

        return Math.max(Math.max(left, right), 0) + start.val;
    }
}

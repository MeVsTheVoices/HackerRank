package cs497.midterm1.averageoflevels;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import cs497.midterm1.TreeNode;

class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        // We're going to run breadth first search to solve our problem
        // We've written this before
        Queue<TreeNode> queue = new LinkedList<>();

        if (root == null) {
            return new LinkedList<>();
        }

        List<Double> averagePerRow = new LinkedList<>();

        queue.add(root);
        while (queue.size() > 0) {
            int sum = 0;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode currentNode = queue.poll();
                sum += currentNode.val;
                if (currentNode.left != null)
                    queue.add(currentNode.left);
                if (currentNode.right != null)
                    queue.add(currentNode.right);
            }
            averagePerRow.add(Double.valueOf(sum)/ Double.valueOf(size));
        }

        return averagePerRow;
    }
}
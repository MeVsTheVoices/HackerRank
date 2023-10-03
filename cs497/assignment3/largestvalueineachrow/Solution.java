package cs497.assignment3.largestvalueineachrow;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import cs497.assignment3.TreeNode;

class Solution {
    public List<Integer> largestValues(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();

        if (root == null) {
            return new LinkedList<>();
        }

        List<Integer> highestPerRow = new LinkedList<>();

        queue.add(root);
        while (queue.size() > 0) {
            int highestSeen = Integer.MIN_VALUE;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode currentNode = queue.poll();
                if (currentNode.val > highestSeen)
                    highestSeen = currentNode.val;
                if (currentNode.left != null)
                    queue.add(currentNode.left);
                if (currentNode.right != null)
                    queue.add(currentNode.right);
            }
            highestPerRow.add(highestSeen);
        }

        return highestPerRow;
    }
}
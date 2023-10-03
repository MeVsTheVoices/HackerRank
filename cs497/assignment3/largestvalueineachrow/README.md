# Intuition
This was a great problem to get to work with after I had a hard time with the last. All we're doing is breadth first search, with a few caveats.

# Approach
- Push the root node on to queue
- For each level in the tree, we, go through only the nodes currently pushed on to our queue, and compare those values to a maximum, if it is greater than the maximum, we keep than, pushing only one value per row on to our accumulating list
- As we go through each of these to compare, we push their left and right children on to the queue, we'll return to those on the next iteration.
- We continue until there are no nodes on the queue, meaning that their were no children on that level

# Complexity
- Time complexity: O(log(n))

- Space complexity: O(log(n))

# Code
```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
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
```
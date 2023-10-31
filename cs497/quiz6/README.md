# Intuition
We map everything on the left to the right once we find the leftmost node. We do this recursively.

# Approach
    - We recursively call the function on the left and right nodes.
    - We set the left node to null.
    - We set the right node to the next largest we found.
    - 

# Complexity
- Time complexity: O(n)

- Space complexity: O(n)
  - We have to store the entire tree in memory.
  - The height of the resultant tree will then be the same as the number of nodes originally.

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
    public TreeNode increasingBST(TreeNode root) {
            if (root == null) {
                return null;
            }
    
            TreeNode left = increasingBST(root.left);
            TreeNode right = increasingBST(root.right);
    
            root.left = null;
    
            root.right = right;
    
            if (left == null) {
                return root;
            }

            TreeNode curr = left;
            while (curr.right != null) {
                curr = curr.right;
            }
    
            curr.right = root;
    
            return left;
    }
}
```
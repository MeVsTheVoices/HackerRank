package cs497.quiz6;

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
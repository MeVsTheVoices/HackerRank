package cs497.assignment3.balancebinarytree;

import java.util.ArrayList;
import java.util.List;

import cs497.assignment3.TreeNode;

class Solution {
    public TreeNode balanceBST(TreeNode root) {
        List<Integer> list = inOrderTraversal(root);
        return recreateBST(list, 0, list.size() - 1);
    }

    ArrayList<Integer> list;
    public List<Integer> inOrderTraversal(TreeNode root) {
        list = new ArrayList<Integer>();
        inOrderTraversalHelper(root);
        return list;
    }
    private void inOrderTraversalHelper(TreeNode root) {
        if (root == null)
            return;
        
        inOrderTraversalHelper(root.left);
        list.add(root.val);
        inOrderTraversalHelper(root.right);
    }

    public TreeNode recreateBST(List<Integer> list, int left, int right) {
        if (left > right)
            return null;

        int mid = (left + right) / 2;
        TreeNode root = new TreeNode(list.get(mid));
        root.left = recreateBST(list, left, mid - 1);
        root.right = recreateBST(list, mid + 1, right);
        return root;
    }
    
}
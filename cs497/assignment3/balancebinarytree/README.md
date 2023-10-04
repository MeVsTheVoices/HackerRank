# Intuition
We're combining a couple things we've done previously. We're going to do an inorder traversal first, we take the results of this, then build another tree.

# Approach
- As mentioned we run an inorder traversal of the tree first
- We then take the results of that traversal
- We recreate the tree using those results

# Complexity
- Time complexity: O(log(n))
    1. We first do an inorder traversal O(log(n))
    2. We then recreate the tree from those results O(log(n))

- Space complexity: O(log(n))
    1. We're going to do an in order traversal O(log(n))
    2. After that we're recreating the tree O(log(n))

# Code
```


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
        System.out.println(root.val);
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
```
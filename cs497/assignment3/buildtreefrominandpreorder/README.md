# Intuition
At first, this seemed easy, I got the idea of divvying things up by looking in the in order traversal, then breaking things in to halves. Getting the bounds right though, entirely another matter.

# Approach
We take the current element, preorder[preleft] and look for the in inorder, we know then that the elements to the left of that index in preorder are in the left subtree. We create that subtree, then move to the right subtree.

# Complexity
- Time complexity: O(n)

- Space complexity: O(log(n))

# Code
```
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildTreeHelper(preorder, inorder, 0, preorder.length - 1, 0, inorder.length - 1);
    }

    
    private TreeNode buildTreeHelper( int[] preorder, int[] inorder, 
                                int preleft, int preright, 
                                int inleft, int inright) {
        if (preleft > preright || inleft > inright)
            return null;
        if (preleft == preright)
            return new TreeNode(preorder[preright]);
        else {
            TreeNode root = new TreeNode(preorder[preleft]);
            int index = indexOf(inorder, preorder[preleft], inleft, inright);
            root.left = buildTreeHelper(preorder, inorder, preleft + 1, preleft + index - inleft, inleft, index - 1);
            root.right = buildTreeHelper(preorder, inorder, preleft + index - inleft + 1, preright, index + 1, inright);
            return root;
        }
    }

    public int indexOf(int[] array, int element, int leftbound, int rightbound) {
        int i;
        for(i = leftbound; i <= rightbound; i++)
            if (array[i] == element)
                return i;
        return -1;
    }

}
```
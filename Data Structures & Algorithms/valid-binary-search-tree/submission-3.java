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
    boolean isValid;
    public boolean isValidBST(TreeNode root) {
        isValid = true;
        checkBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
        return isValid;
    }

    private void checkBST(TreeNode node, int minBound, int maxBound){
        if(node == null) return;

        if(node.val <= minBound || node.val >= maxBound) isValid = false;

        checkBST(node.left, minBound, Math.min(node.val, maxBound));
        checkBST(node.right, Math.max(minBound, node.val), maxBound);
    }
}

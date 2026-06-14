/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) {\ this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val; 
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    static int nGoodNodes;
    public static int goodNodes(TreeNode root) {
        if(root == null) return 0;
        nGoodNodes = 0;
        dfs(root, root.val);
        return nGoodNodes;
    }

    public static void dfs(TreeNode node, int currMax){
        if(node == null) return;

        nGoodNodes += node.val >= currMax ? 1 : 0;
        currMax = Math.max(currMax, node.val);
        dfs(node.left, currMax);
        dfs(node.right, currMax);
    }
}
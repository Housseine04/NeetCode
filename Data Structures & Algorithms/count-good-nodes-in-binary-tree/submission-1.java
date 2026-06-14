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
    public int goodNodes(TreeNode root) {
        if(root == null) return 0;

        Stack<TreeNode> stack = new Stack<>();
        Stack<Integer> maxStack = new Stack<>();
        stack.push(root);
        maxStack.push(root.val);
        int nGoodNodes = 0;

        while(!stack.isEmpty()){
            TreeNode currNode = stack.pop();
            int currMax = maxStack.pop();
            
            if(currNode.val >= currMax){
                nGoodNodes++;
            }
            
            int nextMax = Math.max(currMax, currNode.val);

            if(currNode.right != null) {
                stack.push(currNode.right);
                maxStack.push(nextMax);
            }
            if(currNode.left != null) {
                stack.push(currNode.left);
                maxStack.push(nextMax);
            }
        }
        return nGoodNodes;
    }
}
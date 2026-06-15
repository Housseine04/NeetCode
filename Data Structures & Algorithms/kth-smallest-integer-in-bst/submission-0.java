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
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> arr = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();
        while(root != null){
            stack.push(root);
            root = root.left;
        }

        while(!stack.isEmpty()){
            TreeNode currNode = stack.pop();
            arr.add(currNode.val);
            if(!visited.contains(currNode.val)) visited.add(currNode.val);
            if(currNode.right != null && !visited.contains(currNode.right.val)){
                stack.push(currNode.right);
            }
            if(currNode.left != null && !visited.contains(currNode.left.val)){
                stack.push(currNode.left);
            }

            if(arr.size() == k)break;
        }

        return arr.size() == 0 ? 0 : arr.get(k-1); 
    }

}

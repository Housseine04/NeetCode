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
    public List<Integer> rightSideView(TreeNode root) {
        List<List<Integer>> levels = levelOrder(root);
        List<Integer> result = new ArrayList<>();
        for(List<Integer> sublist : levels){
            result.add(sublist.get(sublist.size() - 1));
        }
        return result;
    }

     public static List<List<Integer>> levelOrder(TreeNode root) {
        //level order :
        /*
        Input: root = [1,2,3,4,5,6,7]
        Output: [[1],[2,3],[4,5,6,7]]
         */
        if(root == null){
            return new ArrayList<>(new ArrayList<>());
        }
        ArrayDeque<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        ArrayList<List<Integer>> result = new ArrayList<>();

        while(!queue.isEmpty()){
            int levelOps = queue.size();
            List<Integer> currList = new ArrayList<>();
            while(levelOps > 0){
                if(queue.isEmpty()) break;
                TreeNode currRoot = queue.poll();
                currList.add(currRoot.val);
                if(currRoot.left != null) queue.offer(currRoot.left);
                if(currRoot.right != null) queue.offer(currRoot.right);
                levelOps--;
            }
            result.add(currList);
        }

        return result;
    }
}

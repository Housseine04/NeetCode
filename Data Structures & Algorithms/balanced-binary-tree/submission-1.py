# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.dfs(root)
        return self.balanced

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:  # leaf
            return 0

        heightLeft = self.dfs(root.left)
        heightRight = self.dfs(root.right)

        if abs(heightLeft - heightRight) > 1:
            self.balanced = False
            
        return 1 + max(heightLeft, heightRight)
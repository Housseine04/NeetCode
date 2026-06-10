# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDiam = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxDiam

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        diamLeft = self.dfs(root.left)
        diamRight = self.dfs(root.right)
        self.maxDiam = max(self.maxDiam, diamLeft+diamRight)

        return 1 + max(diamLeft, diamRight)
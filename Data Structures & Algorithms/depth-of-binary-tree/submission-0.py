# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recordHeights(root, 0)


    def recordHeights(self, root : Optional[TreeNode], currHeight: int) -> int:
        if root is None:
            return currHeight
        left = self.recordHeights(root.left, currHeight + 1)
        right = self.recordHeights(root.right, currHeight+1)
        return max(left,right)
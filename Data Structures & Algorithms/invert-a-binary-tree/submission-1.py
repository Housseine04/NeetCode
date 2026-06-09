# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        headKeeper = root
        self.invertAux(root)
        return headKeeper

    def invertAux(self, root : Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        tmpLeftNode = root.left
        root.left = root.right
        root.right = tmpLeftNode

        self.invertAux(root.left)
        self.invertAux(root.right)

        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    areSame = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and not q is None:
            self.areSame = False
            return self.areSame
        elif q is None and not p is None:
            self.areSame =False
            return self.areSame

        if p is None and q is None:
            return True

        if not p is None and not q is None:
            if p.val != q.val:
                self.areSame = False
            self.isSameTree(p.left, q.left)
            self.isSameTree(p.right, q.right)
        return self.areSame
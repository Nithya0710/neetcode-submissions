# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root==p or root==q:
            return root
        leftRes=self.lowestCommonAncestor(root.left, p, q)
        rightRes=self.lowestCommonAncestor(root.right, p, q)
        if leftRes and rightRes:
            return root
        if leftRes:
            return leftRes
        if rightRes:
            return rightRes
        return None
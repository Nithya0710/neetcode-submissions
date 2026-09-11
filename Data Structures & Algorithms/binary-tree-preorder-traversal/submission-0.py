# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s1=[]
        s2=[]
        if root:
            s1.append(root)
        while s1:
            node=s1.pop()
            s2.append(node)
            if node.right:
                s1.append(node.right)
            if node.left:
                s1.append(node.left)
        res=[]
        while s2:
            res.append(s2.pop().val)
        res.reverse()
        return res
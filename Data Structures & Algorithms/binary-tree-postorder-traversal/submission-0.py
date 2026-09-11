# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack=[]
        curr=root
        prev=None
        res=[]
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            peek=stack[-1]
            if peek.right and prev!=peek.right:
                curr=peek.right
            else:
                node=stack.pop()
                res.append(node.val)
                prev=node
        return res
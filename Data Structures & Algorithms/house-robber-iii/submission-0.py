# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, 0)
            leftRobbed, leftSkipped=dfs(root.left)
            rightRobbed, rightSkipped=dfs(root.right)
            robbed=root.val+leftSkipped+rightSkipped
            skipped=max(leftRobbed, leftSkipped)+max(rightRobbed,rightSkipped)
            return (robbed, skipped)
        robbed, skipped=dfs(root)
        return max(robbed, skipped)
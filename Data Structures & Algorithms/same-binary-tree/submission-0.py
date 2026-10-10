# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1=deque([p])
        q2=deque([q])
        while q1 and q2:
            node1=q1.popleft()
            node2=q2.popleft()
            if not node1 and not node2:
                continue
            elif (node1 and not node2) or (not node1 and node2):
                return False
            elif node1.val!=node2.val:
                return False
            q1.append(node1.left)
            q2.append(node2.left)
            q1.append(node1.right)
            q2.append(node2.right)
        return True
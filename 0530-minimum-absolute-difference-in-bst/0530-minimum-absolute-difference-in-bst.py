# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.m=float('inf')
        self.prev_val=None
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.prev_val is not None:
                self.m=min(self.m,abs(self.prev_val-root.val))
            self.prev_val=root.val
            
            dfs(root.right)
        dfs(root)
        
        return self.m
        
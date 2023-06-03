# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans=0
        def dfs(root):
            
            nonlocal ans
            if not root.left and not root.right:
                return
            
            if (root.val%2)==0:
                if root.left and root.left.left:
                    ans+=root.left.left.val
                if root.left and root.left.right:
                    ans+=root.left.right.val
                
                if root.right and root.right.left:
                    ans+=root.right.left.val
                if root.right and root.right.right:
                    ans+=root.right.right.val
                
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        return ans
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        visited=set()
        ans=[]
        def dfs(root,single):
            
            if not root.left and not root.right:
                ans.append(single)
            if root.left:
                dfs(root.left,single+[root.left.val])
            if root.right:
                dfs(root.right,single+[root.right.val])
        
        dfs(root,[root.val])
        for i in range(len(ans)):
            m=10
            s=ans[i][-1]
            for j in range(len(ans[i])-2,-1,-1):
                s+=ans[i][j]*m
                m*=10
            ans.append(s)
            sm=0
    
        n=len(ans)//2
        for i in range(len(ans)-1,n-1,-1):
            sm+=ans[i]
      
        return sm
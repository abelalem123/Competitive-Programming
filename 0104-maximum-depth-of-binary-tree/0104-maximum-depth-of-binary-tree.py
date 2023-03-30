# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        results=[]
        res=0
        self.finder(root,res,results)
        return max(results)
    
    def finder(self,root,res,results):
        
        if root:
            res+=1
            self.finder(root.left,res,results)
            self.finder(root.right,res,results)
        else:
            results.append(res)
        
    

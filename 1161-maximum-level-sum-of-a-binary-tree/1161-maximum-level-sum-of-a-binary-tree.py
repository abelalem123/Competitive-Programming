# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.ans=1
        self.r=root.val
        q=deque()
       
        q.append([root,1])
        while q:
            sm=0
            level=1
            for _ in range(len(q)):
                s,l=q.popleft()
                level=l
                sm+=s.val
                if s.left:
                    q.append([s.left,l+1])
                if s.right:
                    q.append([s.right,l+1])
            
            if sm>self.r:
                self.ans=level
                self.r=sm
        return self.ans
            
        
        
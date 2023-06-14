# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums=[root.val]
        
        def dfs(root):
            if not root.left and not root.right:
                return
            if root.left:
                nums.append(root.left.val)
                dfs(root.left)
            if root.right:
                nums.append(root.right.val)
                dfs(root.right)
        dfs(root)
        nums.sort()
        m=nums[-1]-nums[0]
        for i in range(1,len(nums)):
            m=min(m,nums[i]-nums[i-1])
        return m
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,left,right,nums):
        if left>right:
            return None
        mid=(left+right)//2
        node=TreeNode(nums[mid])
        node.left=self.helper(left,mid-1,nums)
        node.right=self.helper(mid+1,right,nums)
        return node
    def sortedArrayToBST(self,nums: List[int])->Optional[TreeNode]:
        left=0
        right=len(nums)-1
        return self.helper(left,right,nums)
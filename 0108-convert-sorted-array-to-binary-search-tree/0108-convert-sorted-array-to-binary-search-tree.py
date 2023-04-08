# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self,nums: List[int])->Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        top = TreeNode(nums[mid])
        top.left = self.sortedArrayToBST(nums[:mid])
        top.right = self.sortedArrayToBST(nums[mid+1:])
        return top   
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        m=max(nums)
        mi=nums.index(m)
        node=TreeNode(m)
        node.left=self.constructMaximumBinaryTree(nums[:mi])
        node.right=self.constructMaximumBinaryTree(nums[mi+1:])
        return node
        